import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_left = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_right = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_left.velocity = self.velocity.rotate(angle) * 1.2
        asteroid_right.velocity = self.velocity.rotate(-angle) * 1.2
