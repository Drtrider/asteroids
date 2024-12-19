import pygame
from circleshape import CircleShape
import random
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            # Create new asteroid one
            vector_new_asteroid_one = self.velocity.rotate(random_angle)
            radius_new_asteroid_one = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_one = Asteroid(self.position.x, self.position.y, radius_new_asteroid_one)
            new_asteroid_one.velocity = vector_new_asteroid_one * 1.2

            # Create new asteroid two
            vector_new_asteroid_two = self.velocity.rotate(-random_angle)
            radius_new_asteroid_two = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid_two = Asteroid(self.position.x, self.position.y, radius_new_asteroid_two)
            new_asteroid_two.velocity = vector_new_asteroid_two * 1.2
