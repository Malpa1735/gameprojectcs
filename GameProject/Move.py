import pygame as py
from random import randint
'''
Here we will learn how to move a pygame object/shape
1. Move it and bounce off of the walls
2. Control the movement with keyboard
'''
py.init()
width, height = 600, 600
screen = py.display.set_mode((width, height))
py.display.set_caption("Movement")
clock = py.time.Clock()

run = True
#seting up the background colour

x, y = width/2, height/2
speedX,speedY = 3, 5
c = "#A1B4D6"
while run:
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
    clock.tick(60)
    screen.fill("#e2dede")
    #this makes it move atunomously
    
    
    py.draw.rect(screen, c, (x, y, 50, 50))
    '''
    if x > width - 50 or x < 0:
        speedX = -speedX
        c = (randint(0, 255), randint(0,255), randint(0, 255))
    if y > height - 50 or y < 0:
        speedY = -speedY
        c = (randint(0, 255), randint(0,255), randint(0, 255))
    x += speedX'''
    #y += speedY

    #keymovement
    keys = py.key.get_pressed()#this will create a dictionary called keys
    if keys[py.K_a] and x > 0:
        x -= speedX
    if keys[py.K_d] and x < width - 50:
        x += speedX
    if keys[py.K_w] and y > 0:
        y -= speedY
    if keys[py.K_s] and y < height - 50:
        y += speedY

    #update the screen
    py.display.flip()

py.quit()