import pygame
import os
from settings import *
from game_state import game_state
from assets import load_win_feather, load_enemy_sprite_sheet
from level import act3_platforms
from enemy_data import enemy_config
from enemy import MeleeEnemy, RangedEnemy

feather_rect = pygame.Rect(439, 323, 51, 47)
complete_screen = None
act3_enemies_cache = {}

def handle_act3_logic(screen, player, keys, act3_backgrounds):
    global complete_screen

    screen.blit(act3_backgrounds[game_state['act_index']], (0, 0))
    platforms = act3_platforms[game_state['act_index']]

    # --- Load enemies ONCE per screen using cache ---
    index = game_state['act_index']
    act = game_state['current_act']

    if index not in act3_enemies_cache:
        screen_enemies = []
        if act in enemy_config and index in enemy_config[act]:
            for e in enemy_config[act][index]:
                if e["type"] == "melee":
                    sprites = load_enemy_sprite_sheet(e["sprite_path"], 2, 1)
                    platform = act3_platforms[index][e["platform_index"]]
                    screen_enemies.append(MeleeEnemy(platform, sprites, 0))
                elif e["type"] == "ranged":
                    sprites = load_enemy_sprite_sheet(e["sprite_path"], 3, 1)
                    projectile = sprites[2]
                    screen_enemies.append(RangedEnemy(e["x"], e["y"], sprites[:2], projectile))
        act3_enemies_cache[index] = screen_enemies
    else:
        screen_enemies = act3_enemies_cache[index]

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

    for enemy in screen_enemies:
        if isinstance(enemy, RangedEnemy):
            enemy.update(player)
        else:
            enemy.update()
        enemy.check_collision(player)
        enemy.draw(screen)

    # Feather logic on umber10 (index 9)
    if game_state['act_index'] == 9 and not game_state['feather_collected']:
        if 'feather_img_act3' not in game_state:
            game_state['feather_img_act3'] = pygame.transform.scale(load_win_feather(), (51, 47))
        screen.blit(game_state['feather_img_act3'], feather_rect.topleft)

        if player.get_feet_rect().colliderect(feather_rect):
            game_state['feather_collected'] = True
            game_state['cutscene_idle_started'] = pygame.time.get_ticks()

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
            game_state['act_unlocked'][3] = True
            game_state['act_unlocked'][2] = False
            player.reset_position(x=74,y=200)

    return screen_enemies