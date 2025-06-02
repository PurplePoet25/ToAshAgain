import pygame
from settings import *
from game_state import game_state
from assets import load_totem_sprite
import random
import os

anim_sheet = None

def load_anim_sheet():
    global anim_sheet
    base_path = os.path.dirname(os.path.abspath(__file__))  # current file location
    asset_path = os.path.join(base_path, "..", "assets", "powers", "anim.png")
    anim_sheet = pygame.image.load(asset_path).convert_alpha()

def get_anim_frame(index):
    frame_w, frame_h = anim_sheet.get_width() // 3, anim_sheet.get_height() // 2
    col = index % 3
    row = index // 3
    raw = anim_sheet.subsurface(pygame.Rect(col * frame_w, row * frame_h, frame_w, frame_h))
    return pygame.transform.scale(raw, (57, 41))

ANIM_FRAMES = {
    "mending": 0,
    "gravity": 1,
    "1up": 2,
    "ember": 3,
    "drift": 4,
    "pulse": 5,
}

totem_sprites = {}
active_effects = []
ember_projectiles = []
falling_totems = []

if "power_inventory" not in game_state:
    game_state["power_inventory"] = [None, None, None]

inventory_slots = [
    pygame.Rect(735, 114, 44, 48),
    pygame.Rect(736, 174, 44, 48),
    pygame.Rect(737, 232, 44, 48)
]

def get_offset_x(base_offset):
    if game_state.get("using_alternate"):
        facing = game_state.get("facing_right", True)
        return base_offset + (20 if facing else -20)
    return base_offset

def load_totem_sprites():
    global totem_sprites
    def scaled(name):
        return pygame.transform.scale(load_totem_sprite(name), (51, 47))

    totem_sprites = {
        "mending": scaled("mendingtotem.png"),
        "gravity": scaled("gravitytotem.png"),
        "1up": scaled("1up.png"),
        "ember": scaled("embertotem.png"),
        "drift": scaled("drifttotem.png"),
        "pulse": scaled("pulsetotem.png"),
    }

def add_to_inventory(power_name):
    for i in range(3):
        if game_state["power_inventory"][i] is None:
            game_state["power_inventory"][i] = power_name
            break

def get_totem_sprite(name):
    return totem_sprites.get(name)

def draw_inventory(screen, inv_img):
    if not game_state["reading"]:
        return
    screen.blit(inv_img, (670, 90))
    for i in range(3):
        power = game_state["power_inventory"][i]
        if power:
            icon = pygame.transform.scale(totem_sprites[power], (44, 48))
            screen.blit(icon, inventory_slots[i].topleft)

def add_power(power_name, platforms=None):
    spawn_x = random.randint(50, SCREEN_WIDTH - 80)
    if platforms and isinstance(platforms[0], tuple):
        platforms = [pygame.Rect(*p) for p in platforms]

    falling_totems.append({
        "sprite": get_totem_sprite(power_name),
        "screen": game_state["act_index"] if game_state["current_act"] > 0 else game_state["screen_index"],
        "name": power_name,
        "x": spawn_x,
        "y": -60,
        "vy": 0,
        "platforms": platforms,
        "landed": False,
        "spawn_time": pygame.time.get_ticks()  # ⏰ track when it was dropped
    })

def use_power(index, player, enemies):
    power = game_state["power_inventory"][index]
    if not power:
        return

    if power == "mending":
        if game_state["player_health"] < 5:
            game_state["player_health"] += 1
            spawn_effect("mending", get_offset_x(player.x + 12), player.y - 50, duration=500)

    elif power == "1up":
        if game_state["player_lives"] < 4:
            game_state["player_lives"] += 1
            spawn_effect("1up", get_offset_x(player.x + 12), player.y - 50, duration=500)

    elif power == "gravity":
        game_state["stomp_mode"] = "gravity"
        game_state["stomp_start_time"] = pygame.time.get_ticks()
        game_state["ignore_next_damage"] = True
        spawn_effect("gravity", get_offset_x(player.x + 12), player.y - 50, duration=600)

    elif power == "ember":
        ember_projectiles.append({
            "x": player.x + (60 if player.facing_right else -10),
            "y": player.y + 20 if not player.is_jumping else player.y,
            "vx": 5 if player.facing_right else -5,
            "vy": -6,
            "bounces": 0,
            "sprite": get_anim_frame(ANIM_FRAMES["ember"]),
        })
        game_state["power_inventory"][index] = None  # Remove the totem immediately

    elif power == "drift":
        game_state["drifting"] = True
        game_state["drift_timer"] = pygame.time.get_ticks()
        game_state["drift_ignore_damage"] = True
        player.dash_target_x = player.x + (200 if player.facing_right else -200)
        spawn_effect("drift", get_offset_x(player.x), player.y + 30, duration=500)

    elif power == "pulse":
        for enemy in enemies:
            if hasattr(enemy, "take_damage"):
                spawn_effect("pulse", enemy.x + enemy.width // 2 - 20, enemy.y - 20, duration=600)
                enemy.take_damage()
            elif enemy.alive:
                spawn_effect("pulse", enemy.x + enemy.width // 2 - 20, enemy.y - 20, duration=600)
                enemy.alive = False

    game_state["power_inventory"][index] = None

def spawn_effect(name, x, y, duration=600):
    if name == "gravity":
        return
    if name in ["mending", "1up", "drift", "pulse"]:
        x = get_offset_x(x)
    active_effects.append({
        "sprite": get_anim_frame(ANIM_FRAMES[name]),
        "x": x,
        "y": y,
        "duration": duration,
        "start": pygame.time.get_ticks()
    })

def update_power_effects(screen, player):
    now = pygame.time.get_ticks()
    for effect in active_effects[:]:
        if now - effect["start"] > effect["duration"]:
            active_effects.remove(effect)
        else:
            screen.blit(effect["sprite"], (effect["x"], effect["y"]))

    if (
        game_state.get("stomp_mode") == "gravity"
        and "stomp_start_time" in game_state
        and now - game_state["stomp_start_time"] <= 5000
    ):
        crown = get_anim_frame(ANIM_FRAMES["gravity"])
        screen.blit(crown, (get_offset_x(player.x + 12), player.y - 50))

def update_falling_totems(screen, player):
    current_screen = (
        game_state["act_index"] if game_state["current_act"] > 0
        else game_state["screen_index"]
    )

    visible_totems = [t for t in falling_totems if t["screen"] == current_screen]

    # Limit: skip drawing if already 3 on screen
    if len(visible_totems) >= 3:
        return

    # Use a copy for safe iteration
    for totem in falling_totems[:]:

        if totem["screen"] != current_screen:
            continue  # ❌ Skip totems not on this screen

        # ❌ Despawn if older than 10 seconds
        if pygame.time.get_ticks() - totem.get("spawn_time", 0) > 10000:
            falling_totems.remove(totem)
            continue

        totem["vy"] += GRAVITY
        totem["y"] += totem["vy"]

        rect = pygame.Rect(totem["x"], totem["y"], 40, 40)
        for plat_rect in totem["platforms"]:
            if rect.colliderect(plat_rect) and totem["vy"] >= 0:
                if rect.bottom - totem["vy"] <= plat_rect.top + 5:
                    totem["y"] = plat_rect.top - 40
                    totem["vy"] = 0
                    break

        screen.blit(totem["sprite"], (totem["x"], totem["y"]))

        pickup_box = pygame.Rect(player.x + 10, player.y + 20, 60, 100)
        if pickup_box.colliderect(rect):
            add_to_inventory(totem["name"])
            falling_totems.remove(totem)

def get_closest_enemy(player, enemies):
    min_dist = float('inf')
    closest = None
    for enemy in enemies:
        if not enemy.alive:
            continue
        dist = abs(enemy.x - player.x)
        if dist < min_dist:
            min_dist = dist
            closest = enemy
    return closest

def update_ember_projectiles(screen, enemies, platforms):
    global ember_projectiles
    for proj in ember_projectiles[:]:
        proj['x'] += proj['vx']
        proj['vy'] += GRAVITY * 0.4
        proj['y'] += proj['vy']

        proj_rect = pygame.Rect(proj['x'], proj['y'], 30, 30)

        # Platform bounce logic
        for plat in platforms:
            if proj_rect.colliderect(plat) and proj['vy'] > 0:
                proj['y'] = plat.top - 30
                proj['vy'] = -abs(proj['vy']) * 0.6
                proj['bounces'] += 1
                break

        # Remove if bounced too much
        if proj['bounces'] >= 3:
            ember_projectiles.remove(proj)
            continue

        # Collision with enemies or boss
        for enemy in enemies:
            if proj_rect.colliderect(enemy.get_rect()):
                if hasattr(enemy, "take_damage"):
                    enemy.take_damage()
                elif hasattr(enemy, "alive") and enemy.alive:
                    enemy.alive = False
                ember_projectiles.remove(proj)
                break

        screen.blit(proj['sprite'], (proj['x'], proj['y']))
