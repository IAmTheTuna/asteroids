# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
        #creating groups to manage objects
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()
    print("Updatable group size:", len(updatable))
    print("Drawable group size:", len(drawable))
    
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print('Game Over!')
                sys.exit()
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    asteroid.split()
                    bullet.kill()
                    
        screen.fill('black')
        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
