import pygame
import os
import sys
from settings import *

# === Set absolute asset directory ===
script_dir = os.path.dirname(os.path.abspath(__file__))

# === Sprite Sheet Loader ===
def load_sprite_sheet(relative_path, columns, rows):
    # Resolve full path from relative asset path like "assets/sprites/spritesheet.png"
    full_path = os.path.abspath(os.path.join(script_dir, "..", relative_path))
    sheet = pygame.image.load(full_path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    frame_width = sheet_width // columns
    frame_height = sheet_height // rows

    return [
        sheet.subsurface(pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
        for row in range(rows) for col in range(columns)
    ]

# === Backgrounds ===
def load_home_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "home"))
    filenames = [
        "background-2.png",
        "background-1.png",
        "background1.png",
        "background2.png",
        "background3.png"
    ]
    return _load_backgrounds(folder, filenames)

def load_act1_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "act1"))
    filenames = [f"green{i}.png" for i in range(1, 11)]
    return _load_backgrounds(folder, filenames)

def load_act2_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "act2"))
    filenames = [f"blue{i}.png" for i in range(1, 11)]
    return _load_backgrounds(folder, filenames)

def load_act3_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "act3"))
    filenames = [f"umber{i}.png" for i in range(1, 11)]
    return _load_backgrounds(folder, filenames)

def load_act4_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "act4"))
    filenames = [f"red{i}.png" for i in range(1, 11)]
    return _load_backgrounds(folder, filenames)

def load_win_backgrounds():
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "win"))
    filenames = ["purple-1.png", "purple0.png", "purple1.png"]
    return _load_backgrounds(folder, filenames)

def load_cutscene_backgrounds():
    filenames = ["cutscene1.png", "cutscene2.png", "cutscene3.png"]
    folder = os.path.abspath(os.path.join(script_dir, "..", "assets", "backgrounds", "win"))
    return [pygame.image.load(os.path.join(folder, name)).convert_alpha() for name in filenames]

def _load_backgrounds(folder, filenames):
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
    return images

# === Sprites ===
def load_main_sprite_sheet():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "sprites", "spritesheet.png"))
    return load_sprite_sheet(path, 4, 2)

def load_alt_sprite_sheet():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "sprites", "spritesheet2.png"))
    return load_sprite_sheet(path, 4, 2)

# === Inventory ===
def load_inventory_panel():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "inventory_panel.png"))
    return pygame.image.load(path).convert_alpha()

# === UI Elements ===
def load_title_image():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "title.png"))
    return pygame.transform.scale(pygame.image.load(path).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

def load_enter_popup():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "enterpopup.png"))
    return pygame.image.load(path).convert_alpha()

def load_entering_act_screen():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "entering_act.png"))
    return pygame.image.load(path).convert()

def load_act_complete_screen():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "act_complete.png"))
    return pygame.transform.scale(pygame.image.load(path).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

def load_healthbar_frames():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "healthbar.png"))
    sheet = pygame.image.load(path).convert_alpha()
    frame_height = sheet.get_height() // 6
    return [
        sheet.subsurface(pygame.Rect(0, i * frame_height, sheet.get_width(), frame_height))
        for i in range(6)
    ]

def load_lives_image():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "lives.png"))
    return pygame.image.load(path).convert_alpha()

def load_death_messages():
    msg1 = pygame.image.load(os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "deathmessage1.png"))).convert_alpha()
    msg2 = pygame.image.load(os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "deathmessage2.png"))).convert_alpha()
    return msg1, msg2

def load_win_feather():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "winfeather.png"))
    return pygame.image.load(path).convert_alpha()

def load_shift_popup():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "shiftpopup.png"))
    return pygame.image.load(path).convert_alpha()

def load_left_arrow():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "leftarrow.png"))
    return pygame.image.load(path).convert_alpha()
def load_enemy_sprite_sheet(path, cols, rows):
    full_path = os.path.abspath(os.path.join(script_dir, "..", path))
    return load_sprite_sheet(full_path, cols, rows)


def load_totem_sprite(name):
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "powers", name))
    return pygame.image.load(path).convert_alpha()

def load_bossbar():
    path = os.path.abspath(os.path.join(script_dir, "..", "assets", "ui", "bossbar.png"))
    return pygame.image.load(path).convert_alpha()
