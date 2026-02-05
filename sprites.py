import pygame as pg
from pygame.sprite import Sprite
import settings
from pygame.math import Vector2 as vec


class Player(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.WHITE)
        self.rect = self.image.get_rect()
        self.accel = vec(0,0)
        self.vel = vec(0,0)
        self.pos = vec(x,y)

    def get_keys(self):
        """Set acceleration from input; diagonal is normalized so speed is consistent."""
        self.accel = vec(0, 0)
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            self.accel.y -= 1
        if keys[pg.K_s]:
            self.accel.y += 1
        if keys[pg.K_a]:
            self.accel.x -= 1
        if keys[pg.K_d]:
            self.accel.x += 1
        if self.accel.length_squared() > 0:
            self.accel = self.accel.normalize() * settings.PLAYER_ACCELERATION

    def update(self, dt):
        self.get_keys()
        # Car-like: velocity accumulates from acceleration, friction slows you down
        self.vel += self.accel * dt
        # Friction (velocity decay)
        speed = self.vel.length()
        if speed > 0:
            friction = 1 - settings.PLAYER_FRICTION * dt
            friction = max(0, friction)
            self.vel *= friction
        # Cap speed
        if self.vel.length() > settings.PLAYER_MAX_SPEED:
            self.vel.scale_to_length(settings.PLAYER_MAX_SPEED)
        self.pos += self.vel * dt
        self._check_walls()
        self.rect.center = self.pos

    def _check_walls(self):
        """Keep player in bounds and bounce with equal and opposite velocity on wall hit."""
        half = settings.TILESIZE / 2
        # Left wall
        if self.pos.x < half:
            self.pos.x = half
            self.vel.x = -self.vel.x
            self.accel.x = -self.accel.x
        # Right wall
        if self.pos.x > settings.WIDTH - half:
            self.pos.x = settings.WIDTH - half
            self.vel.x = -self.vel.x
            self.accel.x = -self.accel.x
        # Top wall
        if self.pos.y < half:
            self.pos.y = half
            self.vel.y = -self.vel.y
            self.accel.y = -self.accel.y
        # Bottom wall
        if self.pos.y > settings.HEIGHT - half:
            self.pos.y = settings.HEIGHT - half
            self.vel.y = -self.vel.y
            self.accel.y = -self.accel.y
    
    def check_collision(self, other):
        if self.rect.colliderect(other.rect):
            return True
        return False

    def check_collision_with_enemies(self):
        for enemy in self.game.enemies:
            if self.rect.colliderect(enemy.rect):
                return True
        return False

class Enemy(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.enemies
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((settings.TILESIZE, settings.TILESIZE))
        self.image.fill(settings.RED)
        self.rect = self.image.get_rect()
        self.accel = vec(0, 0)
        self.vel = vec(0, 0)
        self.pos = vec(x, y)

    def _seek_player(self):
        """Steering towards player; limited accel so momentum can carry us past on a juke."""
        to_player = self.game.player.pos - self.pos
        dist_sq = to_player.length_squared()
        if dist_sq < 1:
            self.accel = vec(0, 0)
            return
        desired_vel = to_player.normalize() * settings.ENEMY_MAX_SPEED
        steering = desired_vel - self.vel
        if steering.length_squared() > settings.ENEMY_ACCELERATION ** 2:
            steering.scale_to_length(settings.ENEMY_ACCELERATION)
        self.accel = steering

    def update(self, dt):
        self._seek_player()
        # Car-like: velocity accumulates from acceleration, friction slows you down
        self.vel += self.accel * dt
        # Friction (velocity decay)
        speed = self.vel.length()
        if speed > 0:
            friction = 1 - settings.ENEMY_FRICTION * dt
            friction = max(0, friction)
            self.vel *= friction
        # Cap speed
        if self.vel.length() > settings.ENEMY_MAX_SPEED:
            self.vel.scale_to_length(settings.ENEMY_MAX_SPEED)
        self.pos += self.vel * dt
        self._check_walls()
        self.rect.center = self.pos

    def _check_walls(self):
        """Keep player in bounds and bounce with equal and opposite velocity on wall hit."""
        half = settings.TILESIZE / 2
        # Left wall
        if self.pos.x < half:
            self.pos.x = half
            self.vel.x = -self.vel.x
            self.accel.x = -self.accel.x
        # Right wall
        if self.pos.x > settings.WIDTH - half:
            self.pos.x = settings.WIDTH - half
            self.vel.x = -self.vel.x
            self.accel.x = -self.accel.x
        # Top wall
        if self.pos.y < half:
            self.pos.y = half
            self.vel.y = -self.vel.y
            self.accel.y = -self.accel.y
        # Bottom wall
        if self.pos.y > settings.HEIGHT - half:
            self.pos.y = settings.HEIGHT - half
            self.vel.y = -self.vel.y
            self.accel.y = -self.accel.y