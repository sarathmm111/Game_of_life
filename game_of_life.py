import random
import time
import copy
def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        grid.append(row)
    return grid

def print_grid(grid):
    alive ="."
    dead = " "
    for row in grid:
        print(" ".join([alive if cell else dead for cell in row]))

def count_neighbors(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbors = [(x-1, y-1), (x-1, y), (x-1, y+1),
                (x, y-1),               (x, y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1)]
    count = 0
    for nx, ny in neighbors:
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
            count += 1
    return count

def next_generation(current_grid):
    rows, cols = len(current_grid), len(current_grid[0])
    new_grid = copy.deepcopy(current_grid)
    for x in range(rows):
        for y in range(cols):
            cell = current_grid[x][y]
            neighbors = count_neighbors(current_grid, x, y)
            if cell == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[x][y] = 0
            else:
                if neighbors == 3:
                    new_grid[x][y] = 1
    return new_grid
