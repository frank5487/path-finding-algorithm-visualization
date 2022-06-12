from Constants import *
import pygame

from Grid import Grid
from PathAlgorithm import PathAlgorithm

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("draw test")

def draw(win, spots, grid):
    win.fill(WHITE)

    for row in spots:
        for spot in row:
            spot.draw(win)

    grid.draw_grid_line()
    pygame.display.update()

def get_clicked_pos(pos, rows, cols, width, height):
    col_interval = width // cols
    row_interval = height // rows
    x, y = pos
    row = y // row_interval
    col = x // col_interval
    
    return row, col

def main(win, rows, cols, width, height):
    grid = Grid(rows, cols, width, height, win)
    # print(f'rows: {grid.rows}, cols: {grid.cols}, width: {grid.width}, height: {grid.height}, col_width: {grid.col_interval}, row_height: {grid.row_interval}')
    spots = grid.get_spots()

    start, end = None, None

    run = True
    while run:
        draw(win, spots, grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # left click
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, cols, width, height)
                spot = spots[row][col]
                if not start and spot != end:
                    start = spot
                    start.set_start()
                elif not end and spot != start:
                    end = spot
                    end.set_end()
                elif spot != end and spot != start:
                    spot.set_barrier()

            # right click
            elif pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, rows, cols, width, height)
                spot = spots[row][col]
                spot.reset()
                if spot == start:
                    start = None
                elif spot == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in spots:
                        for spot in row:
                            spot.update_neighbors(spots)
                    PathAlgorithm(lambda: draw(win, spots, grid), spots, start, end).a_star()
                    PathAlgorithm(lambda: draw(win, spots, grid), spots, start, end).dijkstra()
                    PathAlgorithm(lambda: draw(win, spots, grid), spots, start, end).bfs()
                # press c to reset
                elif event.key == pygame.K_c:
                    start = None
                    end = None
                    spots = Grid(rows, cols, width, height, win).get_spots()

if __name__=='__main__':
    main(WIN, ROWS, COLS, WIDTH, HEIGHT)