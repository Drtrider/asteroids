import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_collisions(self,circle_shape_obj):
        r1 = self.radius
        r2 = circle_shape_obj.radius
        distance_diff = pygame.math.Vector2.distance_to(self.position,circle_shape_obj.position)

        if distance_diff > r1 + r2:
            return False
        else:
            return True