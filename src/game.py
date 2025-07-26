import pygame
from .ball import Ball
from settings import *
class Game:
    def __init__(self, _scr,_clock):
        self.scr = _scr
        self.running = True  # ← БЕЗ ":="
        self.clock = _clock

    def run(self):
     ball = Ball(False,400,300,BALL_ANGLE, BALL_SPEED)
     while self.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False  # ← БЕЗ ":="
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("⬅ Нажал влево")
                ball.reflect()
           
        self.scr.fill((0, 0, 0))
        ball.draw(self.scr)

        pygame.display.flip()
        self.clock.tick(FPS)

    pygame.quit()
        
    

   
      
      