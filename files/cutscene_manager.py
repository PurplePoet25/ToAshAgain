import pygame
from settings import *
from game_state import game_state
from level import cutscene_platforms
import math

def handle_cutscene_logic(screen, cutscene_backgrounds, player_main, player_alt):
    if 'cutscene_screen_index' not in game_state:
        game_state['cutscene_screen_index'] = 0
    idx = game_state['cutscene_screen_index']

    # === End after screen 3 ===
    if idx >= 3:
        if not game_state.get('transitioning_to_win'):
            game_state['transitioning_to_win'] = True
            game_state['transition_timer'] = pygame.time.get_ticks()
            game_state['playing_cutscene'] = False
        return

    scaled_bg = pygame.transform.scale(cutscene_backgrounds[idx], (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))
    platforms = cutscene_platforms[idx]

    now = pygame.time.get_ticks()
    game_state.setdefault('cutscene_timer', now)
    game_state.setdefault('main_x', -100)
    game_state.setdefault('alt_x', -200)
    game_state.setdefault('main_y', 459)
    game_state.setdefault('alt_y', 459)
    game_state.setdefault('main_hop_phase', 0)
    game_state.setdefault('alt_hop_phase', 0)
    game_state.setdefault('main_hop_progress', 0)
    game_state.setdefault('alt_hop_progress', 0)
    game_state.setdefault('hop_start_time', now)
    # removed alt_ready_time delay
    if 'alt_ready_time' in game_state: del game_state['alt_ready_time']

    # Fixed path positions
    walk_end_x = 566
    hop_start_x = 540
    hop_end_x = 650
    post_hop_walk_end_x = 620 + 182
    hop_peak = 90

    # === Screen 1 logic ===
    if idx == 0:
        # Main walk
        if game_state['main_hop_phase'] == 0:
            if game_state['main_x'] < hop_start_x:
                game_state['main_x'] += 2.5
                game_state['main_y'] = platforms[0].top - 128
            else:
                game_state['main_hop_phase'] = 1
                game_state['main_hop_progress'] = 0

        elif game_state['main_hop_phase'] == 1:
            game_state['main_hop_progress'] += 0.015
            prog = min(game_state['main_hop_progress'], 1)
            game_state['main_x'] = hop_start_x + (hop_end_x - hop_start_x) * prog
            base_y = platforms[0].top - 128
            game_state['main_y'] = base_y - math.sin(prog * math.pi * 0.75) * hop_peak
            if prog >= 1:
                game_state['main_hop_phase'] = 2

        elif game_state['main_hop_phase'] == 2:
            if game_state['main_x'] < post_hop_walk_end_x:
                game_state['main_x'] += 2.5
                game_state['main_y'] = platforms[1].top - 128  # reaffirmed

        # Alt walk
        if game_state['alt_hop_phase'] == 0 and game_state['alt_x'] < hop_start_x:
            game_state['alt_x'] += 2.3
            game_state['alt_y'] = platforms[0].top - 128
        elif game_state['alt_hop_phase'] == 0:
            if game_state['alt_x'] < hop_start_x:
                game_state['alt_x'] += 2.5
                game_state['alt_y'] = platforms[0].top - 128
            else:
                game_state['alt_hop_phase'] = 1
                game_state['alt_hop_progress'] = 0

        elif game_state['alt_hop_phase'] == 1:
            game_state['alt_hop_progress'] += 0.015
            prog = min(game_state['alt_hop_progress'], 1)
            game_state['alt_x'] = hop_start_x + (hop_end_x - hop_start_x) * prog
            base_y = platforms[0].top - 128
            game_state['alt_y'] = base_y - math.sin(prog * math.pi * 0.75) * hop_peak
            if prog >= 1:
                game_state['alt_hop_phase'] = 2

        elif game_state['alt_hop_phase'] == 2:
            if game_state['alt_x'] < post_hop_walk_end_x:
                game_state['alt_x'] += 2.5
                game_state['alt_y'] = platforms[1].top - 128  # reaffirmed
            else:
                game_state['cutscene_screen_index'] += 1
                for key in list(game_state.keys()):
                    if key.startswith(('main_', 'alt_', 'hop_')):
                        game_state.pop(key, None)
                return

    else:
        game_state['main_x'] += 2.5
        game_state['alt_x'] += 2.5
        game_state['main_y'] = platforms[0].top - 128
        game_state['alt_y'] = platforms[0].top - 128

        if game_state['main_x'] > SCREEN_WIDTH:
            game_state['cutscene_screen_index'] += 1
            for key in list(game_state.keys()):
                if key.startswith(('main_', 'alt_', 'hop_')):
                    game_state.pop(key, None)
            return

    player_main.x = game_state['main_x']
    player_main.y = game_state['main_y']
    player_alt.x = game_state['alt_x']
    player_alt.y = game_state['alt_y']

    player_main.facing_right = True
    player_main.is_jumping = False
    player_main.vy = 0
    player_main.animate(False, True)
    player_main.draw(screen)

    player_alt.facing_right = True
    player_alt.is_jumping = False
    player_alt.vy = 0
    player_alt.animate(False, True)
    wider = pygame.transform.scale(player_alt.current_frame, (player_alt.current_frame.get_width() + 60, player_alt.current_frame.get_height()))
    screen.blit(wider, (player_alt.x, player_alt.y))


