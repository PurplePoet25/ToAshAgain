SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

GRAVITY = 0.8
JUMP_VELOCITY_MAIN = -16
JUMP_VELOCITY_ALT = -14
MOVE_SPEED = 5
GROUND_LEVEL = 560

MAX_JUMPS_MAIN = 2
MAX_JUMPS_ALT = 2
FRAME_DELAY = 6

SHIFT_COOLDOWN_FRAMES = FPS * 4  # cooldown for switching characters
FLY_DURATION_FRAMES = FPS * 1    # 1 second of flight
FLIGHT_COOLDOWN_FRAMES = FPS * 5 # cooldown before flight can be reused

ASSET_DIR = 'assets'
FALL_DAMAGE_Y = 650  # y position that triggers fall damage

# --- Screen Index Mapping ---
TITLE_SCREEN = 0
MAIN_HUB_SCREEN = 2
ACT_SELECT_SCREEN = 4
ACT1_SCREEN = 4
ACT2_SCREEN = 10
ACT3_SCREEN = 16
FINAL_ACT_SCREEN = 22

ACT1_START_INDEX = 999  # Or any large number you’re using for act screens


DROP_RATES_BY_ACT = {
    0: {  # Home (fairly balanced)
        "mending": 0.2,
        "1up": 0.2,
        "gravity": 0.15,
        "ember": 0.15,
        "drift": 0.15,
        "pulse": 0.15,
    },
    1: {  # Act 1 (early healing + intro to powers)
        "mending": 0.25,
        "1up": 0.1,
        "gravity": 0.2,
        "ember": 0.25,
        "drift": 0.1,
        "pulse": 0.1,
    },
    2: {  # Act 2 (flight + agility)
        "mending": 0.1,
        "1up": 0.1,
        "gravity": 0.1,
        "ember": 0.1,
        "drift": 0.4,
        "pulse": 0.2,
    },
    3: {  # Act 3 (heavy gravity + intensity)
        "mending": 0.1,
        "1up": 0.1,
        "gravity": 0.35,
        "ember": 0.25,
        "drift": 0.1,
        "pulse": 0.1,
    },
    4: {  # Act 4 (needs survival & offense)
        "mending": 0.05,
        "1up": 0.25,       # ✅ boosted
        "gravity": 0.1,
        "ember": 0.25,
        "drift": 0.2,
        "pulse": 0.15,
    }
}
