import pygame
from src.ball import Ball
from src.brick import Brick 

from src.paddle import Paddle
from settings import *
class Game:
    def __init__(self, _scr,_clock):
        self.scr = _scr
        self.running = True
        self.clock = _clock
        self.objects = []

    def run(self):
  
     self.objects.extend([Ball(True,SCREEN_WIDTH/2,SCREEN_HEIGHT/2,BALL_ANGLE, BALL_SPEED), Paddle(PADDLE_WIDTH,PADDLE_HEIGHT,10,100, 560,SCREEN_WIDTH),Brick(400,300,100,20)])
     # 0-ball,1-paddle,2-brick
    
     while self.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.objects[0].start()
           
        self.scr.fill((0, 0, 0))
        self.objects[2].draw(self.scr)
        self.objects[1].draw(self.scr)
        self.objects[0].draw(self.scr,self.objects)
        
        pygame.display.flip()
        self.clock.tick(FPS)

    pygame.quit()
        
    

   
      
      