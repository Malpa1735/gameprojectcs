import pygame as py
import random
from obstacle import Obstacle
py.init()
obstaclelist = [] 
GRID_SIZE = 9
CELL_SIZE = 60
WIDTH = GRID_SIZE * CELL_SIZE
HEIGHT = GRID_SIZE * CELL_SIZE
grid_r, grid_c = 9, 9
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)  # start/end color
oImg = py.image.load('tree.png')
oImg = py.transform.scale(oImg,(60,60))
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Path Guaranteed Grid")

# Create empty grid (all walls)
grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

start = (0, 4)
end = (8, 4)

def draw_grid(grid:list):
    index = 0
    for row in range(grid_r):
        for col in range(grid_c):
            x = col * CELL_SIZE
            y = row * CELL_SIZE
            
            if grid[row][col] == 0:    
                obstaclelist[index].draw(screen)
                index += 1
            col += 1 
            if col == grid_c: 
                row += 1 
                col = 0


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
grid = carve_path(grid, start, end)
add_random_openings(grid, 0.35)
for r in range(grid_r):
    for c in range(grid_c):
        if grid[r][c] == 0:
            obstaclelist.append(Obstacle(c*CELL_SIZE, r*CELL_SIZE,oImg))
# Main loop
running = True
while running:
    screen.fill(WHITE)

    # for row in range(GRID_SIZE):
    #     for col in range(GRID_SIZE):
    #         x = col * CELL_SIZE
    #         y = row * CELL_SIZE

    #         if grid[row][col] == 0:
    #             py.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
    #         else:
    #             py.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))

    #         py.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE), 1)

    # Highlight start and end
    py.draw.rect(screen, GREEN, (start[0]*CELL_SIZE, start[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    py.draw.rect(screen, GREEN, (end[0]*CELL_SIZE, end[1]*CELL_SIZE, CELL_SIZE, CELL_SIZE))
    draw_grid(grid)
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    py.display.flip()

py.quit()