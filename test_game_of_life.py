import game_of_life

def test_create_grid():
    rows = 5
    cols = 5
    grid = game_of_life.create_grid(rows, cols)
    assert len(grid) == rows
    for row in grid:
        assert len(row) == cols
        
def test_print_grid(capsys):
    grid = [
        [1, 0, 1],
        [0, 1, 0],
        [1, 1, 1]
    ]
    expected_output = ".   .\n  .  \n. . .\n"
    game_of_life.print_grid(grid)
    captured = capsys.readouterr()
    assert captured.out == expected_output
    
def test_count_neighbors():
    grid = [[1, 0, 1],
            [0, 1, 0],
            [1, 1, 1]]
    x, y = 1, 1
    count = game_of_life.count_neighbors(grid, x, y)
    assert count == 5

