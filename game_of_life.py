import random

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


