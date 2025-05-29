import pygame
from settings import *
from game_state import game_state


class Player:
    def __init__(self, frames, max_jumps, can_glide=False):
        self.frames = [pygame.transform.smoothscale(f, (140, 128)).convert_alpha() if can_glide else pygame.transform.smoothscale(f, (80, 128)).convert_alpha() for f in frames]
        self.x, self.y = 100, GROUND_LEVEL - 128
        self.vy, self.jump_count = 0, 0
        self.is_jumping, self.facing_right = False, True
        self.frame_index, self.frame_timer = 0, 0
        self.walk_frames = [self.frames[0], self.frames[1], self.frames[6]]
        self.current_frame = self.frames[4]
        self.max_jumps, self.can_glide = max_jumps, can_glide
        self.jump_key_released = True
        self.is_gliding = False
        self.is_flying = False
        self.fly_timer = 0
        self.flight_start_time = 0
        self.last_jump_time = 0
        self.flight_opportunity_open = False
        self.space_held_since_last_jump = False
        self.last_flight_end_time = -float('inf')
        self.flight_cooldown = FLIGHT_COOLDOWN_FRAMES * 1000 // FPS
        self.last_damage_time = 0
        self.damage_cooldown = 1000  # milliseconds (1 second)


    def update_sprite(self, frames, max_jumps, can_glide):
        self.frames = [pygame.transform.smoothscale(f, (140, 128)).convert_alpha() if can_glide else pygame.transform.smoothscale(f, (80, 128)).convert_alpha() for f in frames]
        self.walk_frames = [self.frames[0], self.frames[1], self.frames[6]]
        self.current_frame = self.frames[4]
        self.max_jumps, self.can_glide = max_jumps, can_glide
        self.jump_count = 0
        self.is_jumping = False
        self.jump_key_released = True
        self.is_gliding = False
        self.is_flying = False
        self.flight_opportunity_open = False
        self.space_held_since_last_jump = False
        self.last_flight_end_time = -float('inf')

    def get_rect(self):
        return pygame.Rect(self.x, self.y, 80, 128)

    def jump(self, space_held):
        now = pygame.time.get_ticks()
        if not self.can_glide:
            if self.jump_count < self.max_jumps:
                self.vy = JUMP_VELOCITY_MAIN
                self.jump_count += 1
                self.is_jumping = True
                self.jump_key_released = False
        else:
            if self.jump_count == 0:
                self.vy = JUMP_VELOCITY_ALT
                self.jump_count = 1
                self.is_jumping = True
                self.last_jump_time = now
                self.flight_opportunity_open = True
            else:
                self.flight_opportunity_open = False

    def start_flight(self):
        now = pygame.time.get_ticks()
        if now - self.last_flight_end_time < self.flight_cooldown:
            return
        self.is_flying = True
        self.flight_start_time = now
        self.jump_count = 2
        self.is_gliding = False
        self.is_jumping = True

    def update_physics(self, space_held, platforms):
        now = pygame.time.get_ticks()

        # --- Gliding / Flying Physics ---
        if self.can_glide:
            if self.flight_opportunity_open and space_held and self.vy > 0:
                self.start_flight()
                self.flight_opportunity_open = False

            if self.is_flying:
                if space_held and (now - self.flight_start_time <= FLY_DURATION_FRAMES * 1000 // FPS):
                    self.vy = -4
                else:
                    self.is_flying = False
                    self.last_flight_end_time = now
                    self.jump_count = 1

            elif self.is_jumping and self.vy > 0 and space_held:
                self.is_gliding = True
                self.vy = min(self.vy + GRAVITY, 2)
            else:
                self.is_gliding = False
                self.vy += GRAVITY
        else:
            self.vy += GRAVITY

        # --- Apply Vertical Motion in Small Steps ---
        steps = int(abs(self.vy)) + 1
        dy = self.vy / steps

        for _ in range(steps):
            self.y += dy
            for p in platforms:
                if self.get_rect().colliderect(p) and self.vy >= 0:
                    if self.get_rect().bottom <= p.top + 5:  # Tighter threshold
                        self.y = p.top - 128  # Align to top of platform
                        self.vy = 0
                        self.is_jumping = False
                        self.jump_count = 0
                        self.jump_key_released = True
                        self.is_gliding = False
                        self.is_flying = False
                        self.fly_timer = 0
                        if hasattr(self, 'fall_start_y'):
                            del self.fall_start_y
                        return  # Exit early after landing

    def move(self, dx):
        self.x += dx

    
    def reset_position(self, x=100, y=GROUND_LEVEL - 220):
        self.x, self.y = x, y
        self.vy, self.jump_count = 0, 0
        self.is_jumping = False
        self.jump_key_released = True
        self.is_gliding = False
        self.is_flying = False
        self.fly_timer = 0
        self.flight_start_time = 0
        self.last_jump_time = 0
        self.flight_opportunity_open = False
        self.space_held_since_last_jump = False
        self.last_flight_end_time = -float('inf')
        self.vy, self.jump_count = 0, 0
        self.is_jumping = False
        self.jump_key_released = True
        self.is_gliding = False
        self.is_flying = False
        self.fly_timer = 0
        self.flight_start_time = 0
        self.last_jump_time = 0
        self.flight_opportunity_open = False
        self.space_held_since_last_jump = False
        self.last_flight_end_time = -float('inf')

    def get_feet_rect(self):
        rect = self.get_rect()
        return pygame.Rect(rect.left + 20, rect.bottom - 5, rect.width - 40, 5)


    def animate(self, reading, moving):
        if reading:
            self.current_frame = self.frames[7]
        elif self.can_glide and (self.is_flying or self.is_gliding):
            self.current_frame = self.frames[3]
        elif self.is_jumping:
            self.current_frame = self.frames[2]
        elif moving:
            self.frame_timer += 1
            if self.frame_timer >= FRAME_DELAY:
                self.frame_index = (self.frame_index + 1) % len(self.walk_frames)
                self.frame_timer = 0
            self.current_frame = self.walk_frames[self.frame_index]
        else:
            self.frame_index, self.frame_timer = 0, 0
            self.current_frame = self.frames[4]

        if not self.facing_right:
            self.current_frame = pygame.transform.flip(self.current_frame, True, False)

    def draw(self, surface):
        surface.blit(self.current_frame, (self.x, self.y))

    def bounce(self):
        self.vy = -10  # You can tweak this value for a stronger/weaker bounce


    def take_damage(self):
        now = pygame.time.get_ticks()
        if not game_state['showing_death'] and now - self.last_damage_time >= self.damage_cooldown:
            game_state['player_health'] -= 1
            self.last_damage_time = now

            # Knockback logic
            if self.facing_right:
                self.x -= 40  # Knock left
            else:
                self.x += 40  # Knock right
            self.vy = -8      # Bounce upward a bit

            if game_state['player_health'] <= 0:
                game_state['player_lives'] -= 1
                game_state['showing_death'] = True



