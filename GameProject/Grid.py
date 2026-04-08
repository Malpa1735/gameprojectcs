from random import randint
import pygame as py
from obstacle import Obstacle
from Player import Player
#to generalise  our grid we use the following variables
py.mixer.init()
coin_sound = py.mixer.Sound("yoda.mp3.mp3")
pipe_sound = py.mixer.Sound("pipe.mp3")
grid_r, grid_c = 9, 9
grid = [[randint(0,4) for i in range(grid_c)] for j in range(grid_r)]
#ensure starting area is always open
grid[0][0] = 1
grid[0][1] = 1  #right neighbour
grid[1][0] = 1  #bottom neighbour

for g in grid:
    print(g)
cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size*grid_c, cell_size*grid_r
panel = 150
coins = 0

oImg = py.image.load('job2.jpg')
oImg = py.transform.scale(oImg,(60,60))
bgImg = py.image.load('background.jpg')
bgImg = py.transform.scale(bgImg,(width,height))
img = py.image.load('placeholder2.jpg')
img = py.transform.scale(img,(60,60))
cImg = py.image.load('bitcoin.jpg')
cImg = py.transform.scale(cImg,(60,60))
pImg = py.image.load('poop.jpg')
pImg = py.transform.scale(pImg,(60,60))
player1 = Player(0,0,img)


obstaclelist = []
for r in range(grid_r):
    for c in range(grid_c):
        if grid[r][c] == 0:
            obstaclelist.append(Obstacle(c*cell_size, r*cell_size,oImg)) 
py.init()
screen = py.display.set_mode((width + panel, height))
py.display.set_caption("Creating grid")
clock = py.time.Clock() 

def draw_grid(grid:list):
    row = 0 #row of grid
    col = 0 #column of grid
    index = 0
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid[row][col] == 0:    #check if grid list has 1
            #if yes then draw the obstacle
            obstaclelist[index].draw(screen)
            index += 1
        elif grid[row][col] == 6:
            screen.blit(cImg,(col * cell_size, row * cell_size))
        elif grid[row][col] == 5:
            screen.blit(pImg,(col * cell_size, row * cell_size))
        col += 1 #then go to the next cell
        if col == grid_c: #if you reach kast column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero



def draw_panel(screen, coins):
    font = py.font.SysFont(None, 30)
    #panel background
    py.draw.rect(screen,"#8BD0CA", (width, 0 , panel, height))
    textSurface = font.render(f"Coins: {player1.coin}", True, "#ffffff")
    screen.blit(textSurface, (width + 20, 40))

def dig():
    if(grid[player1.y//60][player1.x//60]== 3):
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                player1.coin += 1
                coin_sound.play()
                screen.blit(cImg,(player1.x,player1.y))
                grid[player1.y//60][player1.x//60]= 6
    elif(grid[player1.y//60][player1.x//60] in (1,2,4)):# 1 or 2 or 4
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                screen.blit(pImg,(player1.x,player1.y))
                pipe_sound.play()
                grid[player1.y//60][player1.x//60]= 5
#r = img.get_rect()
run = True
while run:
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
        player1.move(screen, grid, event)
        dig()
    screen.blit(bgImg,(0,0))
    draw_panel(screen,coins)
    #update coins
    '''
    How to draw on the screen using grid
    '''
    draw_grid(grid)
    player1.draw(screen)

    
    
    py.display.flip()#update the screen


py.quit