import pygame
from settings import *

def draw_title_screen(screen, title_img):
    screen.blit(title_img, (0, 0))
    pygame.display.flip()

# UPDATED: Accepts individual event instead of consuming the event queue inside
def handle_title_events(play_button, event):
    if event.type == pygame.QUIT:
        return 'quit'
    elif event.type == pygame.MOUSEBUTTONDOWN:
        if play_button.collidepoint(event.pos):
            return 'play'
    return 'stay'

def draw_dim_overlay(surface):
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 120))  # Translucent black using RGBA
    surface.blit(overlay, (0, 0))

def draw_fullscreen_image(surface, image):
    surface.blit(image, (0, 0))
    pygame.display.flip()
