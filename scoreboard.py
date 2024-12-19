import pygame

class Scoreboard(pygame.font.Font):
    def __init__(self, name, size):
        super().__init__(name, size)
        self.score = 0

    def add_points(self, points):
        self.score += points

    def get_score(self):
        return self.score