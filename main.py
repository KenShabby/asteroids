from constants import *
from circleshape import *
from player import *
import pygame

def main():

    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        dt = clock.tick(60)
        dt /= 1000 # convert delta time to seconds
        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        player.update(dt)
        player.draw(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
