# Game of Life
This is a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway.
## Introduction
The Game of Life is a zero-player game, meaning that its progression is determined by its initial state, with no further input. The "universe" of the game is a grid of cells, each of which can be in one of two states: alive or dead. The game evolves through generations, following simple rules based on the states of neighboring cells.
## Features
- Randomly generates an initial grid of cells.
- Prints each generation of the game with a 0.2-second delay.
- Implements the classic rules of the Game of Life.
## Rules
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

## Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/sarathmm111/Game_of_life.git
