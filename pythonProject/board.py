import numpy as np
from config import *
def grid():
    grid = np.zeros((ROWS, COLUMNS))
    return grid
print(np.flip(grid, 0))

def draw_grid():
    for c in range(COLUMNS):
        for r in range(ROWS):
            pg.draw.rect(screen, BLUE, (c*DISC_SIZE, r*DISC_SIZE+DISC_SIZE, DISC_SIZE, DISC_SIZE))
            pg.draw.circle(screen, WHITE, (int(c*DISC_SIZE+DISC_SIZE/2), int(r*DISC_SIZE+DISC_SIZE+DISC_SIZE/2)), DISC_SIZE)

    for c in range(COLUMNS):
        for r in range (ROWS):
            if grid[r][c] == REAL_PLAYER_PIECE:
                pg.draw.circle(screen, RED, (int(c*DISC_SIZE+DISC_SIZE/2), hight-int(r*DISC_SIZE+DISC_SIZE/2)), DISC_RADIUS)
            elif grid[r][c] == AI_PLAYER_PIECE:
                pg.draw.circle(screen, YELLOW, (int(c*DISC_SIZE+DISC_SIZE/2), hight-int(r*DISC_SIZE+DISC_SIZE/2)), DISC_RADIUS)
                pg.display.update()

def is_valid_position(grid, col):
    return grid[ROWS-1][col] == 0

def get_valid_position(grid):
    valid_position = []
    for col in range(COLUMNS):
        if is_valid_position(grid, col):
            valid_position.append(col)
    return valid_position

def set_next_open_row(grid, c):
    for r in range(ROWS):
        if grid[r][c] == 0:
            return r

def search_win_move(grid, piece):
    for c in range(COLUMNS-3):
        for r in range (ROWS):
            if grid[r][c] == piece and grid[r][c+1] == piece \
                    and grid[r][c+2] == piece and grid[r][c+3] == piece:
                return True
    for c in range (COLUMNS):
        for r in range(ROWS - 3):
            if grid[r][c] == piece and grid[r+1][c] == piece \
                    and grid[r+2][c] == piece and grid[r+3][c] == piece:
                return True
    for c in range(COLUMNS-3):
        for r in range(ROWS-3):
            if grid[r][c] == piece and grid[r+1][c+1] == piece \
                    and grid[r+2][c+2] == piece and grid[r+3][c+3] == piece:
                return True
    for c in range(COLUMNS-3):
        for r in range(3, ROWS):
            if grid[r][c] == piece and grid[r-1][c+1] == piece \
                    and grid[r-2][c+2] == piece and grid[r-3][c+3]:
                return True