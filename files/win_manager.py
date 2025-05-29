import pygame
from settings import *
from game_state import game_state

cup_rect = pygame.Rect(490, 420, 120, 120)  # Final cup hitbox

def handle_win_logic(screen, player, keys, backgrounds):
    screen_index = game_state['screen_index']
    screen.blit(backgrounds[screen_index], (0, 0))

    from level import win_platforms
    platforms = win_platforms[screen_index]

    # === Movement input
    moving = False
    if keys[pygame.K_LEFT]:
        player.move(-MOVE_SPEED)
        player.facing_right = False
        moving = True
    elif keys[pygame.K_RIGHT]:
        player.move(MOVE_SPEED)
        player.facing_right = True
        moving = True

    # === Trampoline bounce logic on purple-1
    if screen_index == 0:
        tramp_rect = pygame.Rect(336, 430, 166, 36)
        feet = player.get_feet_rect()

        # Check if player is standing on top of the trampoline
        on_top = (
            abs(feet.bottom - tramp_rect.top) <= 5 and
            tramp_rect.left <= feet.centerx <= tramp_rect.right
        )

        if on_top:
            streak = game_state.get('trampoline_bounce_streak', 0) + 1
            game_state['trampoline_bounce_streak'] = min(streak, 5)  # Max streak 5
            bounce_strength = -12 - (game_state['trampoline_bounce_streak'] * 2)
            player.vy = bounce_strength
            player.jump_count = 0
            player.is_jumping = True
        else:
            game_state['trampoline_bounce_streak'] = 0  # Reset if not on trampoline

    # === Physics + render
    player.update_physics(keys[pygame.K_SPACE], platforms)
    player.animate(game_state['reading'], moving)
    player.draw(screen)

    # === Navigation between purple screens
    if player.x > SCREEN_WIDTH:
        if screen_index < 2:
            game_state['screen_index'] += 1
            player.x = 0
    elif player.x < 0:
        if screen_index > 0:
            game_state['screen_index'] -= 1
            player.x = SCREEN_WIDTH - 80

    # === Final Cup Interaction (purple2)
    if screen_index == 2:
        if player.get_feet_rect().colliderect(cup_rect) and keys[pygame.K_RETURN]:
            if not game_state.get("ending_played"):
                pygame.time.delay(600)
                font = pygame.font.SysFont(None, 60)
                msg = font.render("Thank you for playing!", True, (255, 230, 255))
                screen.fill((25, 10, 50))
                screen.blit(msg, (SCREEN_WIDTH // 2 - msg.get_width() // 2, SCREEN_HEIGHT // 2 - 30))
                pygame.display.flip()
                pygame.time.delay(4000)
                game_state["ending_played"] = True
            else:
                game_state["on_title"] = True
