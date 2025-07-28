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
            # self.surface = pygame.Surface((BALL_SIZE,BALL_SIZE))
            # self.surface.fill((255,255,255))
            self.surface = pygame.Surface((BALL_SIZE, BALL_SIZE), pygame.SRCALPHA)  # включаем прозрачность
            pygame.draw.circle(self.surface, (255, 255, 255), (BALL_SIZE // 2, BALL_SIZE // 2), BALL_SIZE // 2)

    def check_collision(self,paddle_rect,bricks):
        # if self.hb.colliderect(paddle_rect):
        #    return True
        if (self.x <= 0 or self.x + BALL_SIZE >= SCREEN_WIDTH):
            self.reflect("vertical", False)
        elif (self.y <= 0):
            self.reflect("horizontal",False)
        elif (self.hb.colliderect(paddle_rect)):
            self.reflect("horizontal",False) 
           
            self.angle = BALL_MAX_ANGLE - self.change_bounce_angle(BALL_MAX_ANGLE,paddle_rect)
            print(f"current angle: {self.angle}")
        if (self.y > SCREEN_HEIGHT):
            self.reflect("horizontal",True)
        wasCollision = False
        for brick in bricks: 
            if self.hb.colliderect(brick.hitboxes[0]) or self.hb.colliderect(brick.hitboxes[1]):
               self.reflect("horizontal",False)  
               wasCollision = True
               print("Horizontal collision")
            elif self.hb.colliderect(brick.hitboxes[2]) or self.hb.colliderect(brick.hitboxes[3]):
                self.reflect("vertical",False)  
                wasCollision = True
                print("Vertical collision")
            if (wasCollision):
                brick.delete = True
                break
    
   

        
    def change_bounce_angle(self,max_bounce_angle,paddle_hb):
        offset = (self.hb.centerx - paddle_hb.centerx) / (paddle_hb.width / 2)
        print(f"Offset: {offset}")
        return max_bounce_angle * offset 


    def start(self):
        self.isAttached = False         
    def draw(self,scr,objects):
        paddle = objects[1] 
        bricks = objects[2]



        self.check_collision(paddle.hb,bricks)

        if not self.isAttached:
            
          self.x += self.speed * cos(radians(self.angle))
          self.y += -self.speed * sin(radians(self.angle))
        else:
            self.x = paddle.x + (paddle.width/2) - 10
            self.y = paddle.y - BALL_SIZE

          
          
        scr.blit(self.surface, (self.x,self.y))
        self.hb.topleft = (self.x,self.y)
    def reflect(self,collision_type,defeat):
         if(collision_type == "vertical"):
             self.angle = 180 - self.angle
         elif(collision_type == "horizontal"):
             if(defeat):
                 self.isAttached = True 
                 self.angle = BALL_ANGLE
             else:
                 self.angle = -self.angle
         
         
         
