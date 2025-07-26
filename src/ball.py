import pygame
from settings import *
from math import sin, cos, radians  
class Ball:
    def __init__(self,_isAttached, _x,_y,_angle,_speed):
            self.isAttached = _isAttached
            self.x = _x
            self.y = _y 
            self.speed = _speed
            self.angle = _angle
            self.surface = pygame.Surface((20,20))
            self.surface.fill((255,255,255))
    def draw(self,screen):
        # print(f"current y: {self.y}")
        print(f"current angle: {self.angle}")
        if(self.x <= 0 or self.x + 20 >= SCREEN_WIDTH):
          self.reflect("vertical")
        elif(self.y <=0 or self.y + 20 >= SCREEN_HEIGHT):
          self.reflect("horizontal")  
         
        #  print("за границой")
        self.x += self.speed * cos(radians(self.angle))
        self.y += -self.speed * sin(radians(self.angle))
        screen.blit(self.surface, (self.x,self.y))
    def reflect(self,collision_type):
         if(collision_type == "vertical"):
             self.angle = 180 - self.angle
         elif(collision_type == "horizontal"):
             self.angle = -self.angle    
         
         
