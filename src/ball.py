import pygame
from settings import *
from math import sin, cos, radians  
class Ball:
    def __init__(self,_isAttached, _x,_y,_angle,_speed):
            self.isAttached = _isAttached
            self.x = _x
            self.y = _y 
            self.speed = _speed
            self.hb = pygame.Rect(_x,_y, BALL_SIZE,BALL_SIZE)
            self.angle = _angle
            self.surface = pygame.Surface((BALL_SIZE,BALL_SIZE))
            self.surface.fill((255,255,255))
    def check_collision(self,paddle_rect):
        if self.hb.colliderect(paddle_rect):
           print("HOR")
           return True
    def start(self):
        self.isAttached = False   
        print("gfdgfdg")        
    def draw(self,scr,objects):
        # print(f"current y: {self.y}")
        # print(f"current angle: {self.angle}")
        paddle = objects[1] 
       



        if (self.x <= 0 or self.x + BALL_SIZE >= SCREEN_WIDTH):
            self.reflect("vertical", False)
        elif (self.y <= 0):
            self.reflect("horizontal",False)
        elif (self.check_collision(paddle.hb) == True):
           self.reflect("horizontal",False) 
        if (self.y > SCREEN_HEIGHT):
            self.reflect("horizontal",True)

        if not self.isAttached:
            
          self.x += self.speed * cos(radians(self.angle))
          self.y += -self.speed * sin(radians(self.angle))
          print(self.isAttached)
        else:
            self.x = paddle.x + (paddle.width/2) - 10
            self.y = paddle.y - BALL_SIZE
            print(self.isAttached)

          
          
        scr.blit(self.surface, (self.x,self.y))
        self.hb.topleft = (self.x,self.y)
        # pygame.draw.rect(scr, (255,0,0), self.hb, 2)
    def reflect(self,collision_type,defeat):
         if(collision_type == "vertical"):
             self.angle = 180 - self.angle
         elif(collision_type == "horizontal"):
             if(defeat):
                 self.isAttached = True 
                 self.angle = BALL_ANGLE
             else:
                 self.angle = -self.angle
         
         
         
