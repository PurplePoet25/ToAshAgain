import pygame
from settings import FRAME_DELAY, GRAVITY, FPS
from game_state import game_state
import random


class MeleeEnemy:
    def __init__(self, platform_rect, sprites, y_offset, override_size=None):
        self.sprites = sprites if override_size else [pygame.transform.scale(s, (100, 70)) for s in sprites]
        self.platform = platform_rect

        self.width = self.sprites[0].get_width()
        self.height = self.sprites[0].get_height()

        self.x = platform_rect.x
        self.y = platform_rect.y - self.height + y_offset
        self.direction = 1
        self.speed = 2
        self.frame_index = 0
        self.frame_timer = 0
        self.alive = True
        self.projectiles = []

    def get_rect(self):
        sprite = self.sprites[0]
        return pygame.Rect(self.x, self.y, sprite.get_width(), sprite.get_height())
    
    def update(self):
        if not self.alive:
            return
        self.x += self.speed * self.direction
        if self.x <= self.platform.left or self.x + self.width >= self.platform.right:
            self.direction *= -1
        self.frame_timer += 1
        if self.frame_timer >= FRAME_DELAY:
            self.frame_index = (self.frame_index + 1) % len(self.sprites)
            self.frame_timer = 0

    def draw(self, screen):
        if self.alive:
            sprite = self.sprites[self.frame_index]
            if self.direction < 0:
                sprite = pygame.transform.flip(sprite, True, False)
            screen.blit(sprite, (self.x, self.y))

    def check_collision(self, player):
        if not self.alive:
            return

        enemy_rect = self.get_rect()
        player_feet = player.get_feet_rect()
        head_zone = pygame.Rect(self.x + 20, self.y, self.width - 40, 10)  # Only top 10px of head

        if player_feet.colliderect(head_zone) and player.vy > 0:
            self.alive = False
            player.bounce()
        elif player.get_rect().colliderect(enemy_rect):
            player.take_damage()



class RangedEnemy:
    def __init__(self, x, y, sprites, projectile_img):
        self.sprites = [pygame.transform.scale(s, (100, 100)) for s in sprites]
        self.projectile_img = pygame.transform.scale(projectile_img, (50, 50))

        self.x = x
        self.y = y
        self.width = 80
        self.height = 80
        self.facing_right = True

        self.timer = 0
        self.phase = "idle"
        self.projectiles = []
        self.alive = True

    def get_rect(self):
        sprite = self.sprites[0]
        return pygame.Rect(self.x, self.y, sprite.get_width(), sprite.get_height())



    def update(self, player):
        if not self.alive:
            return

        self.facing_right = player.x > self.x
        self.timer += 1

        if self.timer >= FPS:
            self.timer = 0
            if self.phase == "idle":
                self.phase = "shoot"
                self.shoot()
            else:
                self.phase = "idle"

        new_projectiles = []
        for proj in self.projectiles:
            proj['x'] += proj['vx']

            if game_state['current_act'] == 2:
                # Act 2: Straight line, no gravity
                proj['y'] += proj['vy']
            else:
                # Acts 1, 3, 4: Gravity-affected
                proj['vy'] += GRAVITY * 0.4
                proj['y'] += proj['vy']

                if game_state['current_act'] == 4:
                    from level import act4_platforms
                    for plat in act4_platforms[game_state['act_index']]:
                        proj_rect = pygame.Rect(proj['x'], proj['y'], 18, 18)
                        if proj_rect.colliderect(plat) and proj['vy'] > 0:
                            proj['y'] = plat.top - 18
                            proj['vy'] = -proj['vy'] * 0.6
                            proj['bounce_count'] = proj.get('bounce_count', 0) + 1
                            break

            if proj.get('bounce_count', 0) < 4:
                new_projectiles.append(proj)

        self.projectiles = new_projectiles

    def shoot(self):
        offset = 30
        spawn_x = self.x + self.width if self.facing_right else self.x - 18
        spawn_y = self.y + self.height // 2
        vx = 5 if self.facing_right else -5
        vy = -3 if game_state['current_act'] in [1, 3, 4] else 0
        self.projectiles.append({
            'x': spawn_x,
            'y': spawn_y,
            'vx': vx,
            'vy': vy,
            'bounce_count': 0
        })

    def draw(self, screen):
        if not self.alive:
            return

        sprite = self.sprites[0] if self.phase == "idle" else self.sprites[1]
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)
        screen.blit(sprite, (self.x, self.y))

        for proj in self.projectiles:
            img = self.projectile_img
            if proj['vx'] < 0:
                img = pygame.transform.flip(img, True, False)
            screen.blit(img, (proj['x'], proj['y']))

    def check_collision(self, player):
        if not self.alive:
            return

        enemy_rect = self.get_rect()
        player_feet = player.get_feet_rect()
        head_zone = pygame.Rect(self.x + 20, self.y, self.width - 40, 10)  # Only top 10px of head

        if player_feet.colliderect(head_zone) and player.vy > 0:
            self.alive = False
            player.bounce()
        elif player.get_rect().colliderect(enemy_rect):
            player.take_damage()

        for proj in self.projectiles[:]:
            proj_rect = pygame.Rect(proj['x'], proj['y'], 18, 18)
            if proj_rect.colliderect(player.get_rect()):
                player.take_damage()
                self.projectiles.remove(proj)


class BossInfernalVicar:
    def __init__(self, x, y, sprites, platforms):
        self.x = x
        self.y = y
        self.alive = True
        self.sprites = sprites
        self.width = 200
        self.height = 150
        self.health = 6
        self.facing_right = True
        self.projectiles = []
        self.phase = "idle"
        self.frame_timer = 0
        self.death_started = False
        self.death_index = 6
        self.death_timer = 0
        self.last_action_time = 0
        self.last_hit_time = 0
        self.last_shot_time = 0
        self.spawn_time = pygame.time.get_ticks()
        self.shots_fired = 0
        self.landed = True
        self.jumping = False
        self.jump_origin = (0, 0)
        self.jump_target = (0, 0)
        self.jump_start_time = 0
        self.is_boss = True  # ✅ Helps uniquely track boss in drift
        self.allowed_platforms = [
            pygame.Rect(110, 199, 146, 25),
            pygame.Rect(0, 475, 186, 23),
            pygame.Rect(317, 398, 163, 17),
            pygame.Rect(532, 279, 162, 15),
            pygame.Rect(622, 473, 178, 21),
        ]

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def find_closest_platform_to_player(self, player):
        player_center = player.get_rect().center
        return min(self.allowed_platforms, key=lambda plat: abs((plat.left + plat.width // 2) - player_center[0]) + abs((plat.top) - player_center[1]))

    def start_hop_to(self, target_rect):
        self.jump_origin = (self.x, self.y)
        self.jump_target = (
            target_rect.left + target_rect.width // 2 - self.width // 2,
            target_rect.top - self.height  + 20
        )
        self.jump_start_time = pygame.time.get_ticks()
        self.jumping = True
        self.landed = False

    def shoot(self):
        now = pygame.time.get_ticks()
        kind = random.choice(["arc", "straight"])
        offset_x = self.width - 30 if self.facing_right else -30
        vx = 3 if self.facing_right else -3
        vy = -2 if kind == "arc" else 0
        gravity = 0.12 if kind == "arc" else 0
        base_sprite = self.sprites[3] if kind == "arc" else self.sprites[4]
        sprite = base_sprite if self.facing_right else pygame.transform.flip(base_sprite, True, False)
        self.projectiles.append({
            "x": self.x + (self.width - 45 if self.facing_right else -15),
            "y": self.y + 30,
            "vx": vx,
            "vy": vy,
            "gravity": gravity,
            "sprite": sprite
        })
        self.phase = "attack"
        self.last_shot_time = now
        self.frame_timer = now

    def take_damage(self):
        if self.health > 0:
            self.health -= 1
            if self.health <= 0:
                self.phase = "death"
                self.death_started = True
                self.death_index = 6
                self.death_timer = pygame.time.get_ticks()
                self.alive = False

                # Move to dramatic death location (right edge of platform 4)
                plat = pygame.Rect(532, 279, 162, 15)
                self.x = plat.right - self.width
                self.y = plat.top - self.height
            else:
                target = random.choice(self.allowed_platforms)
                self.start_hop_to(target)


    def update(self, player):
        now = pygame.time.get_ticks()

        # Spawn delay
        if now - self.spawn_time < 2000:
            return

        self.facing_right = player.x > self.x

        # --- Dramatic Death Animation ---
        if self.health <= 0:
            if not self.death_started:
                self.death_started = True
                self.death_index = 6
                self.death_timer = now

                # Teleport to platform edge
                plat = pygame.Rect(532, 279, 162, 15)
                self.x = plat.right - self.width
                self.y = plat.top - self.height
            elif self.death_index < 8 and now - self.death_timer >= 800:
                self.death_index += 1
                self.death_timer = now

                # Fire chaotic projectiles to both sides
                for direction in [-1, 1]:
                    kind = random.choice(["arc", "straight"])
                    offset_x = self.width - 30 if direction == 1 else -30
                    vx = 4 * direction
                    vy = -2 if kind == "arc" else 0
                    gravity = 0.12 if kind == "arc" else 0
                    base_sprite = self.sprites[3] if kind == "arc" else self.sprites[4]
                    sprite = base_sprite if direction == 1 else pygame.transform.flip(base_sprite, True, False)
                    self.projectiles.append({
                        "x": self.x + offset_x,
                        "y": self.y + 40,
                        "vx": vx,
                        "vy": vy,
                        "gravity": gravity,
                        "sprite": sprite
                    })

            elif self.death_index >= 8 and now - self.death_timer >= 800:
                game_state['boss_phase'] = 'dead'
            return

        # --- Update all projectiles ---
        for proj in self.projectiles:
            proj["x"] += proj["vx"]
            proj["vy"] += proj["gravity"]
            proj["y"] += proj["vy"]

        # --- Jump Logic ---
        if self.jumping:
            duration = 1200 if self.health > 3 else 700
            t = (now - self.jump_start_time) / duration
            if t >= 1:
                self.x, self.y = self.jump_target
                self.jumping = False
                self.landed = True
                self.last_action_time = now
            else:
                ox, oy = self.jump_origin
                tx, ty = self.jump_target
                self.x = ox + (tx - ox) * t
                arc_height = 60
                self.y = oy + (ty - oy) * t - arc_height * (1 - (2 * t - 1) ** 2)
            return

        # --- Reset to idle after attack ---
        if self.phase == "attack" and now - self.frame_timer > 300:
            self.phase = "idle"

        # --- Shoot or Jump ---
        delay = 6000 if self.health > 3 else 2500
        interval = 1500 if self.health > 3 else 750

        if self.landed:
            if now - self.last_action_time > delay:
                self.landed = False
                closest = self.find_closest_platform_to_player(player)
                if closest:
                    self.start_hop_to(closest)
            elif now - self.last_shot_time > interval:
                self.shoot()


    def draw(self, screen):
        # --- Final Death Frame Animation ---
        if self.health <= 0 and self.death_index <= 8:
            screen.blit(self.sprites[self.death_index], (self.x, self.y + 20))  # ⬅️ shifted
            return

        if self.phase == "death":
            if self.death_index <= 8:
                screen.blit(self.sprites[self.death_index], (self.x, self.y + 20))  # ⬅️ shifted
            if self.death_index == 8:
                game_state['boss_phase'] = 'dead'
            return

        # --- Idle or Attack Sprite ---
        sprite = self.sprites[0 if self.health > 3 else 2] if self.phase == "idle" else self.sprites[1 if self.health > 3 else 5]
        if not self.facing_right:
            sprite = pygame.transform.flip(sprite, True, False)
        screen.blit(sprite, (self.x, self.y))

        # --- Projectiles ---
        for proj in self.projectiles:
            screen.blit(proj["sprite"], (proj["x"], proj["y"]))


    def check_collision(self, player):
        if self.health <= 0:
            return
        boss_rect = self.get_rect()
        player_rect = player.get_rect()
        player_feet = player.get_feet_rect()
        now = pygame.time.get_ticks()

        for proj in self.projectiles[:]:
            proj_rect = pygame.Rect(proj["x"] + 8, proj["y"] + 8, 12, 12)
            if proj_rect.colliderect(player_rect):
                if now - self.last_hit_time > 1000:
                    player.take_damage()
                    self.last_hit_time = now
                self.projectiles.remove(proj)

        head_zone = pygame.Rect(self.x + 30, self.y, self.width - 60, 20)
        if not self.jumping and player_feet.colliderect(head_zone) and player.vy > 0:
            self.take_damage()
            player.bounce()

        elif not self.jumping and player_rect.colliderect(boss_rect):
            if now - self.last_hit_time > 1000:
                player.take_damage()
                self.last_hit_time = now

