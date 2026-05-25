import pygame as py
from dataclasses import dataclass
'''class Obstacle:

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.rect = (self.x, self.y, self.w, self.h) 
    
    
    def draw(self, screen):
        return py.draw.rect(screen, "#000000", self.rect)
    '''
@dataclass
class Obstacle:
    x: int
    y: int
    img: any
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))