import pygame
import sys
import os

# === Background Image Path ===
BG_PATH = r"C:\Users\hasan\Desktop\PixelGame\assets\backgrounds\win\cutscene1.png"
BG_PATH = BG_PATH.encode('unicode_escape').decode('utf-8')

# === Win Feather Path ===
FEATHER_PATH = r"C:\Users\hasan\Desktop\PixelGame\assets\ui\winfeather.png"
FEATHER_PATH = FEATHER_PATH.encode('unicode_escape').decode('utf-8')

# === Inventory Panel Path ===
INV_PATH = r"C:\Users\hasan\Desktop\PixelGame\assets\ui\inventory_panel.png"
INV_PATH = INV_PATH.encode('unicode_escape').decode('utf-8')

# === Pygame Init ===
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform + Feather Aligner")
font = pygame.font.SysFont("Arial", 18)
clock = pygame.time.Clock()

# === Load Images ===
background = pygame.transform.scale(pygame.image.load(BG_PATH), (SCREEN_WIDTH, SCREEN_HEIGHT))
feather_raw = pygame.image.load(FEATHER_PATH).convert_alpha()
inv_img = pygame.image.load(INV_PATH).convert_alpha()

# === Feather Position + Size ===
feather_x, feather_y = 468, 144
feather_width, feather_height = 51, 47
dragging_feather = False

# === Drawing State ===
rectangles = []
drawing = False
start_pos = (0, 0)

running = True
while running:
    screen.blit(background, (0, 0))

    # === Draw Inventory Panel (scaled and positioned like in-game) ===
    scaled_inv = pygame.transform.scale(inv_img, (160, 220))
    screen.blit(scaled_inv, (670, 90))

    # === Draw Feather ===
    feather_img = pygame.transform.scale(feather_raw, (feather_width, feather_height))
    screen.blit(feather_img, (feather_x, feather_y))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(feather_x, feather_y, feather_width, feather_height), 2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                start_pos = event.pos
                drawing = True
                if pygame.Rect(feather_x, feather_y, feather_width, feather_height).collidepoint(event.pos):
                    dragging_feather = True

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if dragging_feather:
                dragging_feather = False
            elif drawing:
                end_pos = event.pos
                x = min(start_pos[0], end_pos[0])
                y = min(start_pos[1], end_pos[1])
                w = abs(end_pos[0] - start_pos[0])
                h = abs(end_pos[1] - start_pos[1])
                rect = pygame.Rect(x, y, w, h)
                rectangles.append(rect)

                print(f"\nAdded: pygame.Rect({x}, {y}, {w}, {h})")
                print("Current Rectangles List:")
                print("[")
                for r in rectangles:
                    print(f"    pygame.Rect({r.x}, {r.y}, {r.width}, {r.height}),")
                print("]")

                with open("platforms_output.txt", "w") as f:
                    f.write("platforms = [\n")
                    for r in rectangles:
                        f.write(f"    pygame.Rect({r.x}, {r.y}, {r.width}, {r.height}),\n")
                    f.write("]\n")

                drawing = False

        elif event.type == pygame.MOUSEMOTION:
            if dragging_feather:
                feather_x, feather_y = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                rectangles.clear()
                print("\nRectangles cleared.")
                with open("platforms_output.txt", "w") as f:
                    f.write("platforms = []\n")
            elif event.key == pygame.K_RETURN:
                print(f"\nFinal Feather Rect:\npygame.Rect({feather_x}, {feather_y}, {feather_width}, {feather_height})")
            elif event.key == pygame.K_UP:
                feather_height += 1
            elif event.key == pygame.K_DOWN:
                feather_height = max(1, feather_height - 1)
            elif event.key == pygame.K_RIGHT:
                feather_width += 1
            elif event.key == pygame.K_LEFT:
                feather_width = max(1, feather_width - 1)

    # === Draw Red Rectangles and Labels ===
    for rect in rectangles:
        pygame.draw.rect(screen, (255, 0, 0), rect, 2)
        label = font.render(f"{rect.topleft} w:{rect.width} h:{rect.height}", True, (255, 255, 255))
        screen.blit(label, (rect.x + 5, rect.y - 20))

    feather_label = font.render(f"feather: ({feather_x}, {feather_y}, {feather_width}, {feather_height})", True, (255, 255, 0))
    screen.blit(feather_label, (10, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
