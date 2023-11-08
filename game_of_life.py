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


