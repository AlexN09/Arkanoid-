import pygame
from src.ball import Ball
from src.brick import Brick 
import math

from src.paddle import Paddle
from settings import *
class Game:
    def __init__(self, _scr,_clock):
        self.scr = _scr
        self.running = True
        self.clock = _clock
        self.objects = []
        
    
    def delete_bricks(self):
       self.objects[2].clear()

    def spawn_bricks(self):
        brick = []
        limit_row = math.floor((SCREEN_WIDTH / BRICK_WIDTH))
        limit_column = math.floor((SCREEN_HEIGHT / BRICK_HEIGHT) - (1/3 * 30))
        interval_row = 0
        interval_column = 0
        for i in range (3,limit_column):
            for j in range (limit_row):
                brick.append(Brick((j * (BRICK_WIDTH+interval_row)),(i * (BRICK_HEIGHT)),BRICK_WIDTH,BRICK_HEIGHT)) 
                print (j * BRICK_WIDTH)
        # brick.append(Brick(460,300,BRICK_WIDTH,BRICK_HEIGHT))
        
        return brick   
    def draw_bricks(self,bricks):
       for i in bricks:
         i.draw(self.scr)
    def display_lives(self):
       live_surf = pygame.Surface((27,27))
       live_surf.fill((255,0,0))
       for i in range(self.objects[0].lives):
          self.scr.blit(live_surf,(650 + (40*i),30))
          
                
    def run(self):
   
     
     self.objects.extend([Ball(True,SCREEN_WIDTH/2,SCREEN_HEIGHT/2,BALL_ANGLE, BALL_SPEED),Paddle(PADDLE_WIDTH,PADDLE_HEIGHT,10,(1/8) * SCREEN_WIDTH, (14/15) * SCREEN_HEIGHT,SCREEN_WIDTH),self.spawn_bricks()])
    
     # 0-ball,1-paddle,2-bricks array
    
     while self.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.objects[0].start()
        for brick in self.objects[2]:
           if brick.delete == True:
              self.objects[2].remove(brick)
        self.scr.fill((0, 0, 0))
        self.draw_bricks(self.objects[2])
        self.objects[1].draw(self.scr)
        self.objects[0].draw(self.scr,self.objects)
        if self.objects[0].lives == 0:
           self.delete_bricks()
           self.objects[2] = self.spawn_bricks()
           self.objects[0].lives = 3
        self.display_lives()
        print(self.objects[0].lives)
        pygame.display.flip()
        self.clock.tick(FPS)

    pygame.quit()
        
    

   
      
      