from settings import MAIN_HUB_SCREEN
import pygame

game_state = {
    # --- ACT & SCREEN TRACKING ---
    'current_act': 0,                 # 0 = Home, 1–4 = Acts
    'act_index': 0,                   # index within the act (0–9)
    'screen_index': MAIN_HUB_SCREEN, # Home screen index

    # --- PLAYER STATS ---
    'player_health': 5,
    'player_lives': 4,
    'showing_death': False,

    # --- UNLOCK SYSTEM ---
    'alt_unlocked': False, #CHANGE
    'just_unlocked_alt': False,
    'act_unlocked': [True, False, False, False], #CHANGE
    'feather_collected': False,

    # --- TRANSITION STATE ---
    'transitioning_to_act': False,
    'transition_timer': 0,
    'transition_target_act': 1,

    # --- CONTROL FLAGS ---
    'player_can_move': True,
    'spawned_on_act_select': False,
    'using_alternate': False,
    'last_shift_time': -float('inf'),
    'reading': False,
    'on_title': True,

    # --- UI FLAGS ---
    'show_shift_popup': False,
    'paused': False,

    # --- CUTSCENE KEYS (Act 2/4) ---
    'is_cutscene': False,
    'cutscene_step': -1,
    'cutscene_timer': 0,
    'showing_act_complete_after_cutscene': False,
    'cutscene_idle_start_time': 0,
    'cutscene_delay_started': False,

    # --- BOSS FIGHT ---
    'boss_phase': 'fight',        # or 'dead'
    'boss_hits': 0,
    'boss_facing_right': True,
    'boss_platform_index': None,
    'boss_on_left_side': True,
    'boss_last_action_time': 0

} 
