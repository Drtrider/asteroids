import pygame

from constants import *
from player import *


def main():
    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    # Creating the player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Init the game and some stuff for it
    pygame.init()
    game_clock = pygame.time.Clock()
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # Set the screen size
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        

    # Update and draw everything
        for group in updatable:
            group.update(dt)

        screen.fill("Black")

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()


        # Controls FPS of the game's window
        current_clock_time = game_clock.tick(60)
        dt = current_clock_time / 1000


if __name__ == "__main__":
    main()
