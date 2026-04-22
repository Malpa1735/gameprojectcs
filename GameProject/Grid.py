from random import randint
import pygame as py
from obstacle import Obstacle
from Player import Player
from Player import Bullets
from Player import Shmaloogle
import time
#to generalise  our grid we use the following variables
py.mixer.init()
coin_sound = py.mixer.Sound("yoda.mp3.mp3")
pipe_sound = py.mixer.Sound("pipe.mp3")
grid_r, grid_c = 9, 9
grid = [[randint(0,4) for i in range(grid_c)] for j in range(grid_r)]
grid[5][4] = 7
grid2 = [[randint(0,1) for i in range(grid_c)]] + [[1 for i in range(grid_c)] for j in range(grid_r - 1)]
#ensure starting area is always open
grid[0][0] = 1
grid[0][1] = 1  #right neighbour
grid[1][0] = 1  #bottom neighbour

for g in grid:
    print(g)
print("go talk to shmallogle")
cell_size = 60 #cell size in which the player will reside
#width and height of the game layout depends on the grid and cell size
width, height = cell_size*grid_c, cell_size*grid_r
panel = 300
coins = 0
sImg = py.image.load('shmaloogle.webp')
spImg = py.transform.scale(sImg,(260,260))
sImg = py.transform.scale(sImg,(60,60))
bImg = py.image.load('bulletbill.webp')
bImg = py.transform.scale(bImg,(60,60))
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
fbgImg = py.image.load('fightbg.jpg')
fbgImg = py.transform.scale(fbgImg,(width,height))
dbgImg = py.image.load('genericds.jpg')
dbgImg = py.transform.scale(dbgImg,(width,height))
player1 = Player(0,0,img)
shmaloogle = Shmaloogle(4*60,5*60,sImg) #best line of code ever?
bulletlist = []
for r in range(grid_r):
    for c in range(grid_c):
        if grid2[r][c] == 0:
            bulletlist.append(Bullets(c*cell_size, r*cell_size,bImg)) 
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
    shmaloogle.draw(screen)
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid[row][col] == 0:    #check if grid list has 1
            #if yes then draw the obstacle
            obstaclelist[index].draw(screen)
            index += 1
        elif grid[row][col] == 3:
            screen.blit(cImg,(col * cell_size, row * cell_size))
        
        '''elif grid[row][col] == 6:
            screen.blit(cImg,(col * cell_size, row * cell_size))
        elif grid[row][col] == 5:
            screen.blit(pImg,(col * cell_size, row * cell_size))'''
        col += 1 #then go to the next cell
        if col == grid_c: #if you reach kast column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero

    

def draw_fight(grid2:list):
    row = 0 #row of grid
    col = 0 #column of grid
    index = 0
    screen.blit(fbgImg,(0,0)) 
    for i in range(grid_r*grid_c): #looping through the entire grid
        if grid2[row][col] == 0:    #check if grid list has 1
            #if yes then draw the obstacle
            bulletlist[index].draw(screen)
            index += 1
        col += 1 #then go to the next cell
        if col == grid_c: #if you reach kast column
            row += 1 #then we go to the next row
            col = 0 #and we reset the column to zero             
fight = False
death = False
def draw_panel(screen, coins):
    font = py.font.SysFont(None, 30)
    #panel background
    py.draw.rect(screen,"#8BD0CA", (width, 0 , panel, height))
    textSurface = font.render(f"Coins: {player1.coin}", True, "#ffffff")
    textSurface2 = font.render(f"HP: {player1.hp}", True, "#ffffff")
    textsurface3 = font.render(f"Shmaloogle HP: {shmaloogle.hp}", True, "#ffffff")
    textSurface4 = font.render(f"Imagine dying.... Idiot", True, "#ffffff")
    screen.blit(textSurface, (width + 20, 40))
    screen.blit(textSurface2, (width + 20, 60))
    if fight == True:
        screen.blit(textsurface3, (width + 20, 240))
        screen.blit(spImg, (width + 20, 250))
    if death == True:
        screen.blit(textSurface4, (width + 20, 240))
        screen.blit(spImg, (width + 20, 250))


def dig():
    global fight
    if(grid[player1.y//60][player1.x//60]== 3):
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                player1.coin += 1
                coin_sound.play()
                #screen.blit(cImg,(player1.x,player1.y))
                grid[player1.y//60][player1.x//60]= 6
    if(grid[player1.y//60][player1.x//60]== 7):
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                time.sleep(2)
                fight = True 
                for g in grid2:
                    print(g)

    
    '''elif(grid[player1.y//60][player1.x//60] in (1,2,4)):# 1 or 2 or 4
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                screen.blit(pImg,(player1.x,player1.y))
                pipe_sound.play()
                grid[player1.y//60][player1.x//60]= 5'''
#r = img.get_rect()
run = True

while run:
    clock.tick(60)
    if fight == False:
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
    if fight == True:
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
            player1.move(screen, grid2, event)
            dig()
        for r in bulletlist:
            r.move(screen, grid2)
        '''
        check one bullet if it reached the bottom bulletList[0].y
        then you generate a new list with 9 places. Replace the 0 with bullets
        and then draw them from x = 0
        ''' 
        if bulletlist[0].y >= 8*cell_size:
            grid2 = [[randint(0,1) for i in range(grid_c)]] + [[1 for i in range(grid_c)] for j in range(grid_r - 1)]
            bulletlist = []
            for r in range(grid_r):
                for c in range(grid_c):
                    if grid2[r][c] == 0:
                        bulletlist.append(Bullets(c*cell_size, r*cell_size,bImg))
        for i in bulletlist:
            player1.collision(i)
            if player1.collide == True:
               player1.hp -= 25
               draw_panel(screen,coins)
               grid2 = [[randint(0,1) for i in range(grid_c)]] + [[1 for i in range(grid_c)] for j in range(grid_r - 1)]
               bulletlist = []
               for r in range(grid_r):
                   for c in range(grid_c):
                       if grid2[r][c] == 0:
                        bulletlist.append(Bullets(c*cell_size, r*cell_size,bImg))

        

        draw_fight(grid2)
    
    if player1.hp == 0:
        fight = False
        death = True
        screen.blit(dbgImg,(0,0))
    
    
    if player1.hp != 0:
        player1.draw(screen)


    
    
    py.display.flip()#update the screen


py.quit