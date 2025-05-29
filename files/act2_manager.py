import pygame
import os

from settings import *
from game_state import game_state
from assets import load_win_feather, load_enemy_sprite_sheet
from level import act2_platforms
from enemy_data import enemy_config
from enemy import MeleeEnemy, RangedEnemy

feather_rect = pygame.Rect(536, 201, 51, 47)

flyin_path = [
    pygame.Rect(387, -116, 0, 0),
    pygame.Rect(200, 12, 0, 0),
    pygame.Rect(443, 122, 0, 0),
    pygame.Rect(102, 310, 0, 0),
]

cutscene_pos = [flyin_path[0].x, flyin_path[0].y]
facing_left = True

# Cutscene frame cache
alt_char_frame_flying = None
alt_char_frame_idle = None
cutscene_frames_loaded = False
complete_screen = None  # cached act_complete screen

act2_enemies_cache = {}  # cache for enemies

def handle_act2_logic(screen, player, keys, act2_backgrounds):
    global cutscene_pos, facing_left
    global alt_char_frame_flying, alt_char_frame_idle, cutscene_frames_loaded, complete_screen

    screen.blit(act2_backgrounds[game_state['act_index']], (0, 0))
    platforms = act2_platforms[game_state['act_index']]

    # --- Load enemies ONCE per screen using cache ---
    index = game_state['act_index']
    act = game_state['current_act']

    if index not in act2_enemies_cache:
        screen_enemies = []
        if act in enemy_config and index in enemy_config[act]:
            for e in enemy_config[act][index]:
                if e["type"] == "melee":
                    sprites = load_enemy_sprite_sheet(e["sprite_path"], 2, 1)
                    platform = act2_platforms[index][e["platform_index"]]
                    screen_enemies.append(MeleeEnemy(platform, sprites, 0))
                elif e["type"] == "ranged":
                    sprites = load_enemy_sprite_sheet(e["sprite_path"], 3, 1)
                    projectile = sprites[2]
                    screen_enemies.append(RangedEnemy(e["x"], e["y"], sprites[:2], projectile))
        act2_enemies_cache[index] = screen_enemies
    else:
        screen_enemies = act2_enemies_cache[index]

    if not game_state['is_cutscene'] and game_state['player_can_move']:
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

    # ✅ Draw feather if not collected
    if game_state['act_index'] == 9 and not game_state['feather_collected'] and not game_state['is_cutscene']:
        if 'feather_img' not in game_state:
            game_state['feather_img'] = pygame.transform.scale(load_win_feather(), (51, 47))
        screen.blit(game_state['feather_img'], feather_rect.topleft)

        if player.get_feet_rect().colliderect(feather_rect):
            game_state['is_cutscene'] = True
            game_state['player_can_move'] = False
            game_state['cutscene_step'] = 0
            game_state['cutscene_timer'] = pygame.time.get_ticks()
            cutscene_pos[:] = [flyin_path[0].x, flyin_path[0].y]
            game_state['cutscene_idle_started'] = False
            game_state['facing_locked'] = False  # Reset

            if not cutscene_frames_loaded:
                alt_sprite_sheet = pygame.image.load(os.path.join(ASSET_DIR, "sprites", "spritesheet2.png")).convert_alpha()
                sheet_w, sheet_h = alt_sprite_sheet.get_size()
                cols, rows = 4, 2
                frame_w, frame_h = sheet_w // cols, sheet_h // rows

                if sheet_w >= frame_w * cols and sheet_h >= frame_h * rows:
                    frame3 = alt_sprite_sheet.subsurface(pygame.Rect(frame_w * 3, frame_h * 0, frame_w, frame_h))
                    frame4 = alt_sprite_sheet.subsurface(pygame.Rect(frame_w * 0, frame_h * 1, frame_w, frame_h))
                    alt_char_frame_flying = pygame.transform.scale(frame3, (125, 128))
                    alt_char_frame_idle = pygame.transform.scale(frame4, (125, 128))
                    complete_img = pygame.image.load(os.path.join(ASSET_DIR, "ui", "act_complete.png")).convert()
                    complete_screen = pygame.transform.scale(complete_img, (SCREEN_WIDTH, SCREEN_HEIGHT))
                    cutscene_frames_loaded = True
                else:
                    print("❌ spritesheet2.png has wrong dimensions for 4x2 grid.")
                    game_state['is_cutscene'] = False
                    return

    if game_state['is_cutscene'] and cutscene_frames_loaded:
        step = game_state['cutscene_step']

        if step < len(flyin_path) - 1:
            target = flyin_path[step + 1]
            dx = target.x - cutscene_pos[0]
            dy = target.y - cutscene_pos[1]
            dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
            speed = 5
            cutscene_pos[0] += speed * dx / dist
            cutscene_pos[1] += speed * dy / dist

            if not game_state.get('facing_locked'):
                facing_left = dx < 0
                if step >= len(flyin_path) - 2:
                    game_state['facing_locked'] = True

            if dist < 4:
                game_state['cutscene_step'] += 1

            sprite = alt_char_frame_flying
            if facing_left:
                sprite = pygame.transform.flip(sprite, True, False)
            screen.blit(sprite, (round(cutscene_pos[0]), round(cutscene_pos[1]) - 7))

        else:
            if not game_state.get('cutscene_idle_started'):
                game_state['cutscene_idle_start_time'] = pygame.time.get_ticks()
                game_state['cutscene_idle_started'] = True

            current_time = pygame.time.get_ticks()
            elapsed = current_time - game_state['cutscene_idle_start_time']

            if elapsed <= 1000:
                sprite = alt_char_frame_idle
                if facing_left:
                    sprite = pygame.transform.flip(sprite, True, False)
                screen.blit(sprite, (round(cutscene_pos[0]), round(cutscene_pos[1]) - 7))
                return

            elif elapsed <= 3000:
                screen.blit(complete_screen, (0, 0))
                pygame.display.flip()
                return

            else:
                game_state['is_cutscene'] = False
                game_state['feather_collected'] = True
                game_state['just_unlocked_alt'] = True
                game_state['current_act'] = 0
                game_state['act_index'] = 0
                game_state['screen_index'] = MAIN_HUB_SCREEN
                game_state['player_can_move'] = True
                game_state['cutscene_idle_started'] = False
                game_state['act_unlocked'][2] = True
                game_state['act_unlocked'][1] = False  # Lock Act 2
                game_state['facing_locked'] = False
                player.reset_position()

    return screen_enemies