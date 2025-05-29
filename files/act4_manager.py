import pygame
import os

from settings import *
from game_state import game_state
from assets import load_win_feather, load_enemy_sprite_sheet
from level import act4_platforms
from enemy_data import enemy_config
from enemy import MeleeEnemy, RangedEnemy, BossInfernalVicar

feather_rect = pygame.Rect(371, 291, 51, 47)
complete_screen = None
act4_enemies_cache = {}

def handle_act4_logic(screen, player, keys, act4_backgrounds):
    global complete_screen

    # === Respawn to screen 8 if boss fight is active and player died ===
    if game_state["current_act"] == 4 and game_state["act_index"] == 9 and game_state.get("showing_death"):
        game_state["act_index"] = 8
        player.reset_position()
        game_state["showing_death"] = False
        if "boss" in game_state:
            game_state["boss"].x = 369
            game_state["boss"].y = 247
            game_state["boss"].spawn_time = pygame.time.get_ticks()

    screen.blit(act4_backgrounds[game_state['act_index']], (0, 0))
    index = game_state['act_index']
    platforms = act4_platforms[index]
    act = game_state['current_act']
    screen_enemies = []

    # === Handle Regular Enemies (screens 0–8) ===
    if index < 9:
        if index not in act4_enemies_cache:
            if act in enemy_config and index in enemy_config[act]:
                for e in enemy_config[act][index]:
                    if e["type"] == "melee":
                        sprites = load_enemy_sprite_sheet(e["sprite_path"], 2, 1)
                        platform = platforms[e["platform_index"]]
                        screen_enemies.append(MeleeEnemy(platform, sprites, 0))
                    elif e["type"] == "ranged":
                        sprites = load_enemy_sprite_sheet(e["sprite_path"], 3, 1)
                        projectile = sprites[2]
                        screen_enemies.append(RangedEnemy(e["x"], e["y"], sprites[:2], projectile))
                act4_enemies_cache[index] = screen_enemies
            else:
                act4_enemies_cache[index] = []
        else:
            screen_enemies = act4_enemies_cache[index]

        for enemy in screen_enemies:
            if isinstance(enemy, RangedEnemy):
                enemy.update(player)
            else:
                enemy.update()
            enemy.check_collision(player)
            enemy.draw(screen)

    # === Boss Fight Logic (screen 9) ===
    elif index == 9:
        if "boss" not in game_state:
            raw_boss_sprites = load_enemy_sprite_sheet("assets/enemies/act4/infernalvicar.png", 5, 2)
            boss_sprites = [pygame.transform.scale(s, (110, 140)) for s in raw_boss_sprites]
            game_state["boss"] = BossInfernalVicar(369, 247, boss_sprites, platforms)
            game_state["boss_phase"] = "fight"
            game_state["feather_collected"] = False

        boss = game_state["boss"]
        if game_state["boss_phase"] != "dead":
            boss.update(player)
            boss.check_collision(player)

            # Prevent boss from walking off screen to the right
            if boss.x + boss.width > SCREEN_WIDTH:
                boss.x = SCREEN_WIDTH - boss.width

        boss.draw(screen)


        # ✅ Append boss to screen_enemies so powers detect it
        screen_enemies.append(boss)

    # === Player Movement ===
    moving = False
    if keys[pygame.K_LEFT]:
        player.move(-MOVE_SPEED)
        player.facing_right = False
        moving = True
    elif keys[pygame.K_RIGHT]:
        player.move(MOVE_SPEED)
        player.facing_right = True
        moving = True

    player.update_physics(keys[pygame.K_SPACE], platforms)
    player.animate(game_state['reading'], moving)
    player.draw(screen)

    # === Feather Logic (only appears after boss dies) ===
    if index == 9 and game_state.get("boss_phase") == "dead" and not game_state['feather_collected']:
        if 'feather_img_act4' not in game_state:
            game_state['feather_img_act4'] = pygame.transform.scale(load_win_feather(), (51, 47))
        screen.blit(game_state['feather_img_act4'], feather_rect.topleft)

        if player.get_feet_rect().colliderect(feather_rect):
            game_state['feather_collected'] = True
            game_state['cutscene_idle_started'] = pygame.time.get_ticks()

    # === Completion Flow ===
    if game_state.get('cutscene_idle_started') and game_state['feather_collected']:
        elapsed = pygame.time.get_ticks() - game_state['cutscene_idle_started']
        if complete_screen is None:
            complete_img = pygame.image.load(os.path.join(ASSET_DIR, "ui", "act_complete.png")).convert()
            complete_screen = pygame.transform.scale(complete_img, (SCREEN_WIDTH, SCREEN_HEIGHT))

        if elapsed <= 2000:
            screen.blit(complete_screen, (0, 0))
        else:
            game_state['cutscene_idle_started'] = None
            game_state['current_act'] = 0
            game_state['act_index'] = 0
            game_state['screen_index'] = MAIN_HUB_SCREEN
            game_state['act_unlocked'] = [False, False, False, False]
            player.reset_position()

    return screen_enemies
