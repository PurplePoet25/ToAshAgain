import pygame
import sys
import os

from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS,
    GRAVITY, JUMP_VELOCITY_MAIN, JUMP_VELOCITY_ALT,
    MOVE_SPEED, GROUND_LEVEL, MAX_JUMPS_MAIN, MAX_JUMPS_ALT,
    FRAME_DELAY, SHIFT_COOLDOWN_FRAMES, FLY_DURATION_FRAMES,
    FLIGHT_COOLDOWN_FRAMES, ASSET_DIR, FALL_DAMAGE_Y,
    MAIN_HUB_SCREEN, TITLE_SCREEN, ACT_SELECT_SCREEN,
    ACT1_SCREEN, ACT2_SCREEN, ACT3_SCREEN, FINAL_ACT_SCREEN,
    ACT1_START_INDEX, DROP_RATES_BY_ACT  # ✅ now included
)
from assets import (
    load_sprite_sheet, load_home_backgrounds, load_act1_backgrounds, load_act2_backgrounds, load_act3_backgrounds,
    load_inventory_panel, load_title_image, load_healthbar_frames, load_lives_image,
    load_death_messages, load_enter_popup, load_shift_popup, load_left_arrow, load_bossbar, load_win_backgrounds, load_act4_backgrounds, load_cutscene_backgrounds
)
from game_state import game_state
from player import Player
from level import core_platforms, act1_platforms, act2_platforms, act3_platforms, act4_platforms
from home_manager import handle_home_screen, handle_home_logic
from act1_manager import handle_act1_logic
from act2_manager import handle_act2_logic
from act3_manager import handle_act3_logic
from act4_manager import handle_act4_logic
from win_manager import handle_win_logic
from cutscene_manager import handle_cutscene_logic
from powers import draw_inventory, update_power_effects, update_falling_totems, use_power, add_power, load_anim_sheet, load_totem_sprites, update_ember_projectiles, falling_totems

# ✅ INIT
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# ✅ Load power sprites AFTER display is initialized
load_anim_sheet()
load_totem_sprites()


pygame.display.set_caption("To Ash Again")
clock = pygame.time.Clock()


backgrounds = load_home_backgrounds()
act1_backgrounds = load_act1_backgrounds()
act2_backgrounds = load_act2_backgrounds()
act3_backgrounds = load_act3_backgrounds()
act4_backgrounds = load_act4_backgrounds()
raw_frames1 = load_sprite_sheet(f"{ASSET_DIR}/sprites/spritesheet.png", 4, 2)
raw_frames2 = load_sprite_sheet(f"{ASSET_DIR}/sprites/spritesheet2.png", 4, 2)
inv_img = load_inventory_panel()
title_img = load_title_image()
healthbar_frames = [pygame.transform.scale(f, (400, 75)) for f in load_healthbar_frames()]
lives_img = load_lives_image()
death_msg1, death_msg2 = load_death_messages()

angel_img = pygame.image.load(os.path.join(ASSET_DIR, "powers", "angel.png")).convert_alpha()
angel_img = pygame.transform.scale(angel_img, (51, 47))
shift_popup_img = pygame.transform.scale(load_shift_popup(), (300, 170))
enter_popup = pygame.transform.scale(load_enter_popup(), (200, 140))
left_arrow = pygame.transform.scale(load_left_arrow(), (120, 80))
angel_rect = pygame.Rect(242, 322, 51, 47)
inv_img_raw = load_inventory_panel()
inv_img = pygame.transform.scale(inv_img_raw, (160, 220))
pause_img = pygame.transform.scale(pygame.image.load(os.path.join(ASSET_DIR, "ui", "pause.png")).convert_alpha(), (480, 519))
win_backgrounds = load_win_backgrounds()
cutscene_backgrounds = load_cutscene_backgrounds()

bossbar_img = load_bossbar()
bossbar_frames = [
    bossbar_img.subsurface(pygame.Rect(0, i * (bossbar_img.get_height() // 7), bossbar_img.get_width(), bossbar_img.get_height() // 7))
    for i in range(7)
]

# === Load both player sprite sheets ===
main_frames = load_sprite_sheet("assets/sprites/spritesheet.png", 4, 2)
alt_frames = load_sprite_sheet("assets/sprites/spritesheet2.png", 4, 2)

# === Main and Alt characters ===
player = Player(main_frames, MAX_JUMPS_MAIN)
alt_character = Player(alt_frames, MAX_JUMPS_ALT)  # Used in cutscene only


play_button = pygame.Rect(SCREEN_WIDTH // 2 - 220, 360, 250, 80)
teacup_zones = [
    pygame.Rect(155, 457, 62, 19),
    pygame.Rect(307, 458, 52, 17),
    pygame.Rect(447, 458, 59, 18),
    pygame.Rect(600, 460, 55, 15),
]

x_offset = SCREEN_WIDTH // 2 - death_msg1.get_width() // 2 + 20
y_offset = 50
respawn_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, y_offset + 200, 300, 80)
exit_button = pygame.Rect(SCREEN_WIDTH // 2 - 150, y_offset + 300, 300, 80)

def align_player_y(platforms, player):
    player_center_x = player.get_rect().centerx
    for p in platforms:
        if p.left <= player_center_x <= p.right:
            player.y = p.top - player.get_rect().height
            break

def apply_player_damage():
    if game_state.get("stomp_mode") == "gravity" and game_state.get("ignore_next_damage"):
        game_state["stomp_mode"] = None
        game_state["ignore_next_damage"] = False
    elif game_state.get("drift_ignore_damage"):
        return  # ✅ skip damage during drift
    else:
        game_state["player_health"] -= 1


def choose_weighted_drop(act):
    rates = DROP_RATES_BY_ACT.get(act, {})
    total = sum(rates.values())
    r = random.uniform(0, total)
    upto = 0
    for power, weight in rates.items():
        if upto + weight >= r:
            return power
        upto += weight
    return None


running = True
while running:
    events = pygame.event.get()
    if game_state['transitioning_to_act']:
        if pygame.time.get_ticks() - game_state['transition_timer'] > 2000:
            game_state['current_act'] = game_state['transition_target_act']
            game_state['act_index'] = 0
            game_state['screen_index'] = ACT1_START_INDEX
            game_state['feather_collected'] = False
            if game_state['transition_target_act'] == 3:
                player.reset_position(y=100)
            else:
                player.reset_position(y=300)
            game_state['transitioning_to_act'] = False
        else:
            img = pygame.image.load(f"{ASSET_DIR}/ui/entering_act.png")
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(FPS)
            continue

    result = handle_home_screen(screen, title_img, play_button, events)
    if result == 'quit':
        break
    elif result == 'stay':
        clock.tick(FPS)
        continue

    keys = pygame.key.get_pressed()
    
# DRIFT dash logic
# ✅ Drift Dash Logic: Damages enemies/bosses in front (only once per drift)
    if game_state.get("drifting"):
        now = pygame.time.get_ticks()
        duration = 300  # milliseconds
        speed = 16

        if "drift_hit_ids" not in game_state:
            game_state["drift_hit_ids"] = set()

        if now - game_state["drift_timer"] < duration:
            dx = speed if player.facing_right else -speed
            player.x += dx
            player.frame_index = 0 if player.facing_right else 1

            drift_hitbox = pygame.Rect(
                player.get_rect().x + (40 if player.facing_right else -60),
                player.get_rect().y + 10,
                70,
                player.get_rect().height - 20
            )

            for enemy in screen_enemies:
                if not enemy.alive:
                    continue

                enemy_key = "boss" if hasattr(enemy, "is_boss") else id(enemy)

                if drift_hitbox.colliderect(enemy.get_rect()) and enemy_key not in game_state["drift_hit_ids"]:
                    if hasattr(enemy, "take_damage"):
                        enemy.take_damage()
                    else:
                        enemy.alive = False
                    game_state["drift_hit_ids"].add(enemy_key)
        else:
            game_state["drifting"] = False
            game_state["drift_ignore_damage"] = False
            game_state["drift_hit_ids"] = set()

    if game_state.get('paused'):
        # Display the pause image
        pause_x = SCREEN_WIDTH // 2 - pause_img.get_width() // 2
        pause_y = SCREEN_HEIGHT // 2 - pause_img.get_height() // 2
        screen.blit(pause_img, (pause_x, pause_y))
        pygame.display.flip()

        # Mini-loop while paused
        while game_state['paused']:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    game_state['paused'] = False

            clock.tick(FPS)
        continue


    for event in events:
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # ⬅️ Place this FIRST so ESC always works
            if event.key == pygame.K_ESCAPE:
                game_state['paused'] = not game_state['paused']

            # ⬇️ Then check movement/gameplay keys only if allowed
            elif game_state['player_can_move'] and not game_state['showing_death']:
                now = pygame.time.get_ticks()
                if event.key == pygame.K_SPACE and not game_state['reading']:
                    player.jump(keys[pygame.K_SPACE])
                elif event.key == pygame.K_LSHIFT and game_state['alt_unlocked']:
                    if now - game_state['last_shift_time'] >= SHIFT_COOLDOWN_FRAMES * 1000 // FPS:
                        game_state['using_alternate'] = not game_state['using_alternate']
                        game_state['last_shift_time'] = now
                        pygame.time.delay(100)
                        if game_state['using_alternate']:
                            player.update_sprite(raw_frames2, MAX_JUMPS_ALT, True)
                        else:
                            player.update_sprite(raw_frames1, MAX_JUMPS_MAIN, False)
                elif event.key in [pygame.K_1, pygame.K_2, pygame.K_3]:
                    if game_state['current_act'] == 0:
                        screen_enemies = []
                    index = [pygame.K_1, pygame.K_2, pygame.K_3].index(event.key)
                    use_power(index, player, screen_enemies)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.jump_key_released = True

        elif event.type == pygame.MOUSEBUTTONDOWN and game_state['showing_death']:
            if game_state['player_lives'] > 0 and respawn_button.collidepoint(event.pos):
                game_state['player_health'] = 5
                game_state['showing_death'] = False
                game_state["stomp_mode"] = None
                game_state["stomp_start_time"] = 0
                if game_state['current_act'] > 0:
                    game_state['act_index'] = 0
                    game_state['screen_index'] = ACT1_START_INDEX

                    if game_state['current_act'] == 1:
                        player.reset_position(x=50, y=300)
                    elif game_state['current_act'] == 2:
                        player.reset_position(x=50, y=250)
                    elif game_state['current_act'] == 3:
                        player.reset_position(x=50, y=100)
                    elif game_state['current_act'] == 4:
                        # Respawn at screen 8 if boss was active
                        if "boss" in game_state and game_state.get("boss_phase") != "dead":
                            game_state['act_index'] = 8
                            player.reset_position(x=50, y=100)
                        else:
                            game_state['act_index'] = 0
                            player.reset_position(x=50, y=100)
                else:
                    game_state['screen_index'] = MAIN_HUB_SCREEN
                    player.reset_position()
            elif game_state['player_lives'] == 0 and respawn_button.collidepoint(event.pos):
                pass
            elif exit_button.collidepoint(event.pos):
                game_state['on_title'] = True
                game_state['showing_death'] = False
                game_state['player_health'] = 5
                game_state['player_lives'] = 4

                # ⬇️ Ensure we always start from Home after exiting
                game_state['current_act'] = 0
                game_state['act_index'] = 0
                game_state['screen_index'] = MAIN_HUB_SCREEN

                # ⬇️ Don't reset act_unlocked — we keep progression
                # game_state['act_unlocked'] remains as is

                player.reset_position()


    game_state['reading'] = keys[pygame.K_r]

    if game_state['showing_death']:
        msg = death_msg1 if game_state['player_lives'] > 0 else death_msg2
        screen.blit(msg, (x_offset, y_offset))
        pygame.display.flip()
        clock.tick(FPS)
        continue

    screen_enemies = []

    if game_state.get("playing_cutscene"):
        handle_cutscene_logic(screen, cutscene_backgrounds, player, alt_character)
        pygame.display.flip()
        clock.tick(FPS)
        continue


    if game_state['current_act'] == 0:
        result = handle_home_logic(screen, player, keys, events, teacup_zones, backgrounds, enter_popup, angel_img, shift_popup_img, angel_rect, left_arrow)
        if result == 'teleporting':
            continue  # prevent rest of the frame logic from running

        if player.x > SCREEN_WIDTH:
            if game_state['screen_index'] < len(backgrounds) - 1:
                game_state['screen_index'] += 1
                player.x = 0
                align_player_y(core_platforms[game_state['screen_index']], player)
        elif player.x < 0:
            if game_state['screen_index'] > 0:
                game_state['screen_index'] -= 1
                player.x = SCREEN_WIDTH - 80
                align_player_y(core_platforms[game_state['screen_index']], player)
        platforms = core_platforms[game_state['screen_index']]

    elif game_state['current_act'] == 1:
        screen_enemies = handle_act1_logic(screen, player, keys, act1_backgrounds)
        if player.x > SCREEN_WIDTH:
            if game_state['act_index'] < len(act1_backgrounds) - 1:
                game_state['act_index'] += 1
                player.x = 0
                align_player_y(act1_platforms[game_state['act_index']], player)
        elif player.x < 0:
            if game_state['act_index'] > 0:
                game_state['act_index'] -= 1
                player.x = SCREEN_WIDTH - 80
                align_player_y(act1_platforms[game_state['act_index']], player)
        platforms = act1_platforms[game_state['act_index']]

    elif game_state['current_act'] == 2:
        screen_enemies = handle_act2_logic(screen, player, keys, act2_backgrounds)
        if player.x > SCREEN_WIDTH:
            if game_state['act_index'] < len(act2_backgrounds) - 1:
                game_state['act_index'] += 1
                player.x = 0
                align_player_y(act2_platforms[game_state['act_index']], player)
        elif player.x < 0:
            if game_state['act_index'] > 0:
                game_state['act_index'] -= 1
                player.x = SCREEN_WIDTH - 80
                align_player_y(act2_platforms[game_state['act_index']], player)
        platforms = act2_platforms[game_state['act_index']]

    elif game_state['current_act'] == 3:
        screen_enemies = handle_act3_logic(screen, player, keys, act3_backgrounds)
        if player.x > SCREEN_WIDTH:
            if game_state['act_index'] < len(act3_backgrounds) - 1:
                game_state['act_index'] += 1
                player.x = 0
                align_player_y(act3_platforms[game_state['act_index']], player)
        elif player.x < 0:
            if game_state['act_index'] > 0:
                game_state['act_index'] -= 1
                player.x = SCREEN_WIDTH - 80
                align_player_y(act3_platforms[game_state['act_index']], player)
        platforms = act3_platforms[game_state['act_index']]

    elif game_state['current_act'] == 4:
        screen_enemies = handle_act4_logic(screen, player, keys, act4_backgrounds)

        # === Boss Health Bar Display on red10 ===
        if game_state['act_index'] == 9 and "boss" in game_state:
            hp = max(0, min(6, 6 - game_state["boss"].health))
            bossbar_scaled = pygame.transform.scale(bossbar_frames[hp], (320, 60))
            screen.blit(bossbar_scaled, (460, 520))


        if player.x > SCREEN_WIDTH:
            if game_state['act_index'] < len(act4_backgrounds) - 1:
                game_state['act_index'] += 1
                player.x = 0
                align_player_y(act4_platforms[game_state['act_index']], player)
        elif player.x < 0:
            if game_state['act_index'] == 9 and "boss" in game_state:
                player.x = 0  # Prevent back-walk if boss active
            elif game_state['act_index'] > 0:
                game_state['act_index'] -= 1
                player.x = SCREEN_WIDTH - 80
                align_player_y(act4_platforms[game_state['act_index']], player)

        platforms = act4_platforms[game_state['act_index']]

    elif game_state['current_act'] == 5:
        handle_win_logic(screen, player, keys, win_backgrounds)

        # === Winning world transition handler
    if game_state.get('transitioning_to_win'):
        if game_state.get("transitioning_to_win"):
            game_state["current_act"] = 5  # ✅ Go to winning world
            game_state["screen_index"] = 1
            game_state["transitioning_to_win"] = False
            game_state["cutscene_screen_index"] = 0
            # Reset player position if needed
            player.reset_position()


            # Align player to ground platform in purple0
            from level import win_platforms
            align_player_y(win_platforms[1], player)

            game_state['transitioning_to_win'] = False



    if player.vy > 0 and not hasattr(player, 'fall_start_y'):
        player.fall_start_y = player.y

    # === VOID CHECK: run BEFORE checking platform collisions ===
    if player.y > SCREEN_HEIGHT and not game_state['showing_death']:
        print("☠️ VOID KILL triggered on screen", game_state['act_index'])
        apply_player_damage()
        if game_state['player_health'] <= 0:
            game_state['player_lives'] -= 1
            game_state['showing_death'] = True

    for p in platforms:
        if player.get_rect().colliderect(p) and player.vy >= 0:
            if player.get_rect().bottom <= p.top + 20:
                fall_distance = player.y - getattr(player, 'fall_start_y', player.y)
                if fall_distance > SCREEN_HEIGHT // 2 and not game_state['showing_death']:
                    if game_state.get("stomp_mode") == "gravity" and game_state.get("ignore_next_damage"):
                        game_state["stomp_mode"] = None
                        game_state["ignore_next_damage"] = False
                    else:
                        apply_player_damage()

                    if game_state['player_health'] <= 0:
                        game_state['showing_death'] = True

                player.y = p.top - 128
                player.vy = 0
                player.is_jumping = False
                player.jump_count = 0
                player.jump_key_released = True
                player.is_gliding = False
                player.is_flying = False
                player.fly_timer = 0
    if hasattr(player, 'fall_start_y'):
        del player.fall_start_y

    



    # ✅ Gravity Totem: Deal -1 HP to closest enemy or boss
    if game_state.get("stomp_mode") == "gravity":
        now = pygame.time.get_ticks()
        if now - game_state["stomp_start_time"] > 5000:
            game_state["stomp_mode"] = None
        else:
            for enemy in screen_enemies:
                if not enemy.alive:
                    continue
                dx = abs((player.x + 40) - (enemy.x + enemy.width // 2))
                dy = abs((player.y + 64) - (enemy.y + enemy.height // 2))
                if dx < 180 and dy < 120:
                    if hasattr(enemy, "take_damage"):
                        enemy.take_damage()
                    else:
                        enemy.alive = False
                    game_state["stomp_mode"] = None
                    break

    # Inventory drawing
    draw_inventory(screen, inv_img)
    update_power_effects(screen, player)
    update_falling_totems(screen, player)
    if screen_enemies is not None:
        update_ember_projectiles(screen, screen_enemies, platforms)
    else:
        update_ember_projectiles(screen, [], platforms)


    # Power Drop Logic
    import random

    # --- Drop Logic ---
    now = pygame.time.get_ticks()
    if "last_drop_time" not in game_state:
        game_state["last_drop_time"] = now
    if "last_screen" not in game_state:
        game_state["last_screen"] = -1

    # Reset drop timer if screen changes
    if game_state["current_act"] > 0:
        current_screen = game_state["act_index"]
    else:
        current_screen = game_state["screen_index"]

    if game_state["last_screen"] != current_screen:
        game_state["last_screen"] = current_screen
        game_state["last_drop_time"] = now

    drop_delay = 6000  # Reduced from 10000

    from powers import falling_totems
    totems_on_screen = [t for t in falling_totems if t["screen"] == current_screen]
    max_totems = 5 if game_state["current_act"] == 0 else 3

    if (
        None in game_state["power_inventory"] and
        len(totems_on_screen) < max_totems and
        not game_state.get('transitioning_to_act') and
        now - game_state["last_drop_time"] > drop_delay
    ):
        game_state["last_drop_time"] = now
        chosen = choose_weighted_drop(game_state["current_act"])
        if chosen:
            add_power(chosen, platforms)




    screen.blit(healthbar_frames[5 - max(0, min(5, game_state['player_health']))], (0, 5))
    frame_height = lives_img.get_height() // 5
    frame_width = lives_img.get_width()
    lives_sub = lives_img.subsurface(pygame.Rect(0, game_state['player_lives'] * frame_height, frame_width, frame_height))
    lives_scaled = pygame.transform.scale(lives_sub, (120, 50))
    screen.blit(lives_scaled, (400, 22))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
