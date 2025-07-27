import pygame 
from settings import * 
from src.game import Game
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.DOUBLEBUF)
pygame.display.set_caption("Arkanoid")

clock = pygame.time.Clock()

game = Game(screen,clock)
game.run()
  
