import pygame as py
import time

class Player:
    '''
    Creates a player with x, y coordinates
    and w, h as its width and height
    '''
    #static/class variables
    
    speedX, speedY = 5, 5
    collide = False
    #constructor
    def __init__(self, x, y, img):
       
        self.x = x
        self.y = y
        self.w = 50
        self.h = 50
        self.img = img
        self.hp = 100
        self.coin = 0
        self.rect = (self.x, self.y, self.w, self.h) 

    def draw(self, screen):
        #blit draws surface on a surface. Here image surface is drawn on the screen
        screen.blit(self.img, (self.x, self.y))
        #py.draw.rect(screen, "#9E0C0C", self.rect)

    # def move(self,screen):
    #     keys = py.key.get_pressed()#this will create a dictionary called keys
    #     if keys[py.K_a] and self.x > 0:
    #         self.x -= Player.speedX    
    #     if keys[py.K_d] and self.x < screen.get_width() - self.w:
    #         self.x += Player.speedX
    #     if keys[py.K_w] and self.y > 0:
    #         self.y -= Player.speedY
    #     if keys[py.K_s] and self.y < screen.get_height() - self.h:
    #         self.y += Player.speedY
    #     #update the rect attribute of the player object
    #     self.rect = (self.x, self.y, self.w, self.h)

    def move(self, screen, grid, event):
        r = self.y//60
        c = self.x//60
        if event.type == py.KEYDOWN:
            if event.key == py.K_a and c - 1 >= 0 and grid[r][c-1] != 0:
                self.x -= 60   
            if event.key == py.K_d and c + 1 < len(grid[0]) and grid[r][c+1] != 0:
                self.x += 60
            if event.key == py.K_w and r- 1 >= 0 and grid[r - 1][c] != 0:
                self.y -= 60
            if event.key == py.K_s and r + 1 < len(grid) and grid[r + 1][c]!= 0:
                self.y += 60
            '''if(grid[self.y//60][self.x//60]== 3):#condition to find coin
                self.coin += 1#if found increase value by 1
                grid[self.y//60][self.x//60]= 1#we change value to register coin as picked up
            #update the rect attribute of the player object'''
            self.rect = (self.x, self.y, self.w, self.h)

    
    def collision(self, obstacle):
        if abs(self.x - obstacle.x) < self.w:
           
            if abs(self.y - obstacle.y) < self.h:
                if (not Player.collide):
                    print("Collision")
                    Player.collide = True
                    return
            
            else:
                Player.collide = False
        else:
            Player.collide = False
                                                                  
class Bullets:
    '''
    Creates objects that damage the player
    '''
    
    speedX, speedY = 5, 5
    collide = False
    #constructor
    def __init__(self, x, y, img):
       
        self.x = x
        self.y = y 
        self.w = 30
        self.h = 30
        self.dmg = 20
        self.img = img
        self.rect = (self.x, self.y, self.w, self.h) 

    def draw(self, screen):
        #blit draws surface on a surface. Here image surface is drawn on the screen
        screen.blit(self.img, (self.x, self.y - 1))

    
    def move(self, screen, grid):
        r = self.y//60 
        c = self.x//60
        if r + 1 < len(grid) and grid[r + 1][c]!= 0:
            self.y += 3
            
        
            
        self.rect = (self.x, self.y, self.w, self.h)