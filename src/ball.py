import pygame

class Ball:
    def __init__(self,_isAttached, _x,_y,_angle,):
            self.isAttached = _isAttached
            self.x = _x
            self.y = _y 
            self.angle = _angle
            self.surface = pygame.Surface((20,20))
            self.surface.fill((255,255,255))
    def draw(self,screen):
        self.x -= 1 
        self.x -= 1
        screen.blit(self.surface, (self.x,self.y))
