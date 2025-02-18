import pygame
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)