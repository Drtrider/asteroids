import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from scoreboard import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    # Score board setup
    scoreboard = Scoreboard(None, 64)

    # font = pygame.font.Font(None, 64)
    # text = font.render("Score: 0", True, "Red", None)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game over!")
                print(f"Final Score: {scoreboard.get_score()}")
                sys.exit()

        # Collision check for shots and asteroids
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    # Split the asteroid
                    asteroid.split()
                    bullet.kill()

                    # Add points based on size killed
                    if asteroid.radius == 60:
                        scoreboard.add_points(1)
                    elif asteroid.radius == 40:
                        scoreboard.add_points(2)
                    else:
                        scoreboard.add_points(3)

        screen.fill("black")

        # Add scoreboard text into the screen
        current_score = scoreboard.get_score()
        scoreboard_render = scoreboard.render(
            f"Score: {current_score}", True, "Red", None)
        textpos = scoreboard_render.get_rect(
            centerx=screen.get_width() / 2, y=10)
        screen.blit(scoreboard_render, textpos)

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
