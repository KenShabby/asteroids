from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
import pygame
from player import Player
from shot import Shot
import sys

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Groupings
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    Player.containers = (updateable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

   # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updateable.update(dt)

        # Check for collisions
        for asteroid in asteroids:
            for shot in shots:  # Shot hits asteroid
                if asteroid.collision(shot):
                    shot.kill()
                    asteroid.split()

            if asteroid.collision(player): # Player hits asteroid
                print("Game over!")
                sys.exit()

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000 # convert delta time to seconds


if __name__ == "__main__":
    main()
