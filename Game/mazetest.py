import pygame as py
from random import randint
from obstacle import Obstacle
import random
cell_size = 60
GRID_SIZE = 9
oImg = py.image.load('tree.png')
oImg = py.transform.scale(oImg,(60,60))
grid_r, grid_c = 9, 9
width, height = cell_size*grid_c, cell_size*grid_r
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
obstaclelist = [] 
start = (0, 4)
end = (8, 4)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
def carve_path(grid, start, end):
    x, y = start
    grid[y][x] = 1

    while (x, y) != end:
        moves = []

        # Bias toward the goal
        if x < end[0]:
            moves.append((x + 1, y))
        if x > end[0]:
            moves.append((x - 1, y))
        if y < end[1]:
            moves.append((x, y + 1))
        if y > end[1]:
            moves.append((x, y - 1))

        # Add some randomness (side steps)
        moves += [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)
        ]

        # Keep valid moves only
        valid_moves = [
            (nx, ny) for (nx, ny) in moves
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE
        ]
        # Choose randomly but biased
        x, y = random.choice(valid_moves)
        grid[y][x] = 1

    return grid

def add_random_openings(grid, chance=0.3):
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if grid[y][x] == 0 and random.random() < chance:
                grid[y][x] = 1

# Generate grid
#grid = carve_path(grid, start, end)
#add_random_openings(grid, 0.35)


py.init()
screen = py.display.set_mode((width , height))
py.display.set_caption("Creating grid")
clock = py.time.Clock() 

def draw_grid(grid:list):
    index = 0
    for row in range(grid_r):
        for col in range(grid_c):
            x = col * cell_size
            y = row * cell_size
            
            if grid[row][col] == 0:    
                obstaclelist[index].draw(screen)
                index += 1
            col += 1 
            if col == grid_c: 
                row += 1 
                col = 0




grid = carve_path(grid, start, end)
add_random_openings(grid, 0.1)
for r in range(grid_r):
    for c in range(grid_c):
        if grid[r][c] == 0:
            obstaclelist.append(Obstacle(c*cell_size, r*cell_size,oImg))
run = True

while run:
    
    
    
    
    clock.tick(60)
    for event in py.event.get():
        if event.type == py.QUIT:
            run = False
            
    #update coins
    '''
    How to draw on the screen using grid
    '''
    draw_grid(grid)


    py.display.flip()
py.quit