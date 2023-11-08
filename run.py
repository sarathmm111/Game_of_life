from game_of_life import *

def main(rows, cols, generations):
    grid = create_grid(rows, cols)
    print("Initial Generation:")
    print_grid(grid)
    for generation in range(generations):
        time.sleep(0.5)
        grid = next_generation(grid)
        print("\033c")
        print_grid(grid)
        
if __name__ == "__main__":
    rows = 20
    cols = 20
    generations = 50
    main(rows, cols, generations)