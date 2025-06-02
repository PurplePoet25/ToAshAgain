import pygame
from assets import load_enter_popup
from settings import *
from game_state import game_state
from screens import draw_title_screen, handle_title_events
import os

def handle_home_screen(screen, title_img, play_button, events):
    if game_state['on_title']:
        draw_title_screen(screen, title_img)
        for event in events:
            result = handle_title_events(play_button, event)
            if result == 'quit':
                return 'quit'
            elif result == 'play':
                game_state['on_title'] = False
        return 'stay'

def handle_home_logic(screen, player, keys, events, teacup_zones, backgrounds, enter_popup, angel_img, shift_popup_img, angel_rect, left_arrow):
    # Draw background
    if game_state['screen_index'] < len(backgrounds):
        screen.blit(backgrounds[game_state['screen_index']], (0, 0))

    # 👈 Show left arrow if Act 2 just finished and we're near the angel screen
    if game_state['just_unlocked_alt'] and game_state['screen_index'] in [1, 2]:
        screen.blit(left_arrow, (33, 98))

    # Movement
    moving = False
    if keys[pygame.K_LEFT]:
        player.move(-MOVE_SPEED)
        player.facing_right = False
        moving = True
    elif keys[pygame.K_RIGHT]:
        player.move(MOVE_SPEED)
        player.facing_right = True
        moving = True

    # Platform collisions
    from level import core_platforms
    platforms = core_platforms[min(game_state['screen_index'], len(core_platforms) - 1)]
    player.update_physics(keys[pygame.K_SPACE], platforms)
    player.animate(game_state['reading'], moving)
    player.draw(screen)

    # Teacup enter popup
    if game_state['screen_index'] == 4:
        for i, zone in enumerate(teacup_zones):
            if player.get_feet_rect().colliderect(zone) and game_state['act_unlocked'][i]:
                screen.blit(enter_popup, (SCREEN_WIDTH - 240, 60))
                if keys[pygame.K_RETURN]:
                    game_state['transition_target_act'] = i + 1
                    game_state['transition_timer'] = pygame.time.get_ticks()
                    game_state['transitioning_to_act'] = True

    # Angel & Shift Popup Logic – Only on screen_index 0
    if game_state['screen_index'] == 0:
        if game_state['just_unlocked_alt']:
            screen.blit(angel_img, angel_rect.topleft)
            if player.get_feet_rect().colliderect(angel_rect):
                game_state['alt_unlocked'] = True
                game_state['just_unlocked_alt'] = False
                game_state['show_shift_popup'] = True

        if game_state['alt_unlocked'] and game_state['show_shift_popup']:
            screen.blit(shift_popup_img, (466, 46))

    # 🌟 Purple Star Drop + Cutscene Trigger (background1)
    if (
        game_state['screen_index'] == 2 and
        all(not unlocked for unlocked in game_state['act_unlocked']) and
        not game_state.get('winning_world_unlocked') and
        not game_state.get('purple_star_collected')
    ):
        if 'purple_star_img' not in game_state:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            star_path = os.path.join(script_dir, "..", "assets", "ui", "purplestar.png")
            raw_star = pygame.image.load(star_path).convert_alpha()

            game_state['purple_star_img'] = pygame.transform.scale(raw_star, (68, 63))
            game_state['purple_star_y'] = -80
            game_state['purple_star_target_y'] = (SCREEN_HEIGHT - 63) // 2

        if game_state['purple_star_y'] < game_state['purple_star_target_y']:
            game_state['purple_star_y'] += 10

        star_x = (SCREEN_WIDTH - 68) // 2
        star_rect = pygame.Rect(star_x, game_state['purple_star_y'], 68, 63)
        screen.blit(game_state['purple_star_img'], star_rect.topleft)

        if abs(game_state['purple_star_y'] - game_state['purple_star_target_y']) <= 10:
            if player.get_feet_rect().colliderect(star_rect):
                game_state['purple_star_collected'] = True
                game_state['playing_cutscene'] = True
                game_state['cutscene_screen_index'] = 0
                game_state['cutscene_jump'] = False
                game_state['main_x'] = 0
                game_state['main_y'] = 0  # Will be aligned in cutscene_manager
                game_state['alt_x'] = -60
                game_state['alt_y'] = 0
                del game_state['purple_star_img']




