import pygame 

class Paddle:
    def __init__(self, _width, _height,_speed, _x,_y,_screen_width):
        self.x = _x 
        self.y = _y
        self.width = _width 
        self.hb = pygame.Rect(_x,_y, _width, _height)
        self.height = _height
        self.screen_width = _screen_width
        self.speed = _speed
        self.surface = pygame.Surface((_width,_height))
        self.surface.fill((255,255,255))

    def draw(self, scr):
     keys = pygame.key.get_pressed()
    
     if keys[pygame.K_RIGHT] and self.x <= self.screen_width - (self.width + 15):
        self.x += self.speed
     elif keys[pygame.K_LEFT] and self.x > 10:
        self.x -= self.speed
     scr.blit(self.surface, (self.x,self.y))        
     self.hb.topleft = (self.x,self.y)
    
     

   

        