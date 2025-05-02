import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill(pygame.Color(0, 0, 0))

        updatable.update(dt)
        for d in drawable:
            d.draw(screen)

        for a in asteroids:
            if player.colliding(a):
                print("Game over!")
                sys.exit()
            for shot in shots:
                if shot.colliding(a):
                    shot.kill()
                    a.split()

        pygame.display.flip()
        dt = clock.tick(60) / 1000 # 60 FPS


if __name__ == "__main__":
    main()

