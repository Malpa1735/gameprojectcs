import pygame as py
py.init()
width, height = 600, 600

screen = py.display.set_mode((width,height))
screen.fill("#bdd2ac")
listCord = [(0,600), (width/2, height/2), (600,0), (600,600),(width/2,height/2)]
run = True
'''for event in py.event.get():
    if event.type == py.QUIT:
        '''