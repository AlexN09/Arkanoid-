import pygame
import random 

class Brick:
    def __init__(self, _x,_y,_width,_height):
        self.x = _x
        self.y = _y 
        self.delete = False
        self.width = _width
        self.height = _height 
        self.surface = pygame.Surface((_width,_height))
        self.surface.fill((Brick.rnd_color()))
        self.hitboxes = [pygame.Rect(_x,_y,_width,2),pygame.Rect(_x,_y + _height,_width,2),pygame.Rect(_x,_y,2,_height),pygame.Rect(_x + _width,_y,2,_height)]  # 0,1-horizontal:2,3-vertical
    def rnd_color():
         base = [255, random.randint(100, 255), random.randint(100, 255)]
         random.shuffle(base)
         return tuple(base)
    def draw(self,scr):
        scr.blit(self.surface,(self.x,self.y))
        j=0
       
        
        
        