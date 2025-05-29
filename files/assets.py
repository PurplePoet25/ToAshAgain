import pygame
import os
import sys
from settings import *

# === Sprite Sheet Loader ===
def load_sprite_sheet(filename, columns, rows):
    sheet = pygame.image.load(filename).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    frame_width = sheet_width // columns
    frame_height = sheet_height // rows
    return [sheet.subsurface(pygame.Rect(col * frame_width, row * frame_height, frame_width, frame_height))
            for row in range(rows) for col in range(columns)]

# === Backgrounds ===
def load_home_backgrounds():
    folder = os.path.join(ASSET_DIR, "backgrounds", "home")
    print("📂 Checking folder:", folder)
    if not os.path.exists(folder):
        print("❌ Folder does not exist!")
        return []

    print("📁 Files inside 'home':", os.listdir(folder))

    filenames = [
        "background-2.png",
        "background-1.png",
        "background1.png",
        "background2.png",
        "background3.png"
    ]
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
        except Exception as e:
            print(f"⚠️ Error loading {name}: {e}")
    print(f"✅ Loaded {len(images)} background(s)")
    return images

def load_act1_backgrounds():
    filenames = [
        "green1.png", "green2.png", "green3.png", "green4.png", "green5.png",
        "green6.png", "green7.png", "green8.png", "green9.png", "green10.png"
    ]
    folder = os.path.join(ASSET_DIR, "backgrounds", "act1")
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
        except Exception as e:
            print(f"⚠️ Error loading {name}: {e}")
    print(f"✅ Loaded {len(images)} Act 1 background(s)")
    return images

def load_act2_backgrounds():
    filenames = [
        "blue1.png", "blue2.png", "blue3.png", "blue4.png", "blue5.png",
        "blue6.png", "blue7.png", "blue8.png", "blue9.png", "blue10.png"
    ]
    folder = os.path.join(ASSET_DIR, "backgrounds", "act2")
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
    print(f"✅ Loaded {len(images)} Act 2 background(s)")
    return images

def load_act3_backgrounds():
    filenames = [
        "umber1.png", "umber2.png", "umber3.png", "umber4.png", "umber5.png",
        "umber6.png", "umber7.png", "umber8.png", "umber9.png", "umber10.png"
    ]
    folder = os.path.join(ASSET_DIR, "backgrounds", "act3")
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
    print(f"✅ Loaded {len(images)} Act 3 background(s)")
    return images

def load_act4_backgrounds():
    filenames = [
        "red1.png", "red2.png", "red3.png", "red4.png", "red5.png",
        "red6.png", "red7.png", "red8.png", "red9.png", "red10.png"
    ]
    folder = os.path.join(ASSET_DIR, "backgrounds", "act4")
    images = []
    for name in filenames:
        path = os.path.join(folder, name)
        try:
            img = pygame.image.load(path).convert()
            img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            images.append(img)
        except FileNotFoundError:
            print(f"❌ File not found: {path}")
        except Exception as e:
            print(f"⚠️ Error loading {name}: {e}")
    print(f"✅ Loaded {len(images)} Act 4 background(s)")
    return images
    
def load_win_backgrounds():
    folder = os.path.join(ASSET_DIR, "backgrounds", "win")
    filenames = ["purple-1.png", "purple0.png", "purple1.png"]
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

def load_cutscene_backgrounds():
    cutscene_paths = [
        os.path.join(ASSET_DIR, "backgrounds", "win", "cutscene1.png"),
        os.path.join(ASSET_DIR, "backgrounds", "win", "cutscene2.png"),
        os.path.join(ASSET_DIR, "backgrounds", "win", "cutscene3.png"),
    ]
    return [pygame.image.load(path).convert_alpha() for path in cutscene_paths]


# === Sprites ===
def load_main_sprite_sheet():
    return load_sprite_sheet(os.path.join(ASSET_DIR, "sprites", "spritesheet.png"), 4, 2)

def load_alt_sprite_sheet():
    return load_sprite_sheet(os.path.join(ASSET_DIR, "sprites", "spritesheet2.png"), 4, 2)

# === Inventory ===
def load_inventory_panel():
    path = os.path.join(ASSET_DIR, "ui", "inventory_panel.png")
    if not os.path.exists(path):
        print(f"❌ Inventory panel not found: {path}")
        sys.exit()
    return pygame.transform.scale(pygame.image.load(path).convert_alpha(), (180, 250))

# === UI ===
def load_title_image():
    return pygame.transform.scale(pygame.image.load(os.path.join(ASSET_DIR, "ui", "title.png")).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

def load_enter_popup():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "enterpopup.png")).convert_alpha()

def load_entering_act_screen():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "entering_act.png")).convert()

def load_act_complete_screen():
    path = os.path.join(ASSET_DIR, "ui", "act_complete.png")
    return pygame.transform.scale(pygame.image.load(path).convert(), (SCREEN_WIDTH, SCREEN_HEIGHT))

def load_healthbar_frames():
    sheet = pygame.image.load(os.path.join(ASSET_DIR, "ui", "healthbar.png")).convert_alpha()
    frame_height = sheet.get_height() // 6
    return [
        sheet.subsurface(pygame.Rect(0, i * frame_height, sheet.get_width(), frame_height))
        for i in range(6)
    ]

# === Misc UI ===
def load_lives_image():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "lives.png")).convert_alpha()

def load_death_messages():
    msg1 = pygame.image.load(os.path.join(ASSET_DIR, "ui", "deathmessage1.png")).convert_alpha()
    msg2 = pygame.image.load(os.path.join(ASSET_DIR, "ui", "deathmessage2.png")).convert_alpha()
    return msg1, msg2

def load_win_feather():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "winfeather.png")).convert_alpha()

def load_shift_popup():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "shiftpopup.png")).convert_alpha()

def load_left_arrow():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "leftarrow.png")).convert_alpha()

def load_enemy_sprite_sheet(path, cols, rows):
    return load_sprite_sheet(path, cols, rows)

def load_totem_sprite(name):
    path = os.path.join(ASSET_DIR, "powers", name)
    return pygame.image.load(path).convert_alpha()

def load_bossbar():
    return pygame.image.load(os.path.join(ASSET_DIR, "ui", "bossbar.png")).convert_alpha()

