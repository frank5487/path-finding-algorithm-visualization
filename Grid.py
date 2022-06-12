from Constants import * 
import pygame

from Spot import Spot

class Grid:
    def __init__(self, rows, cols, width, height, win):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.col_interval = self.width // self.cols
        self.row_interval = self.height // self.rows
        self.spots = []
        self.set_spots()
        pass

    def set_spots(self):
        for i in range(self.rows):
            self.spots.append([])
            for j in range(self.cols):
                spot = Spot(i, j, self.col_interval, self.row_interval, self.rows, self.cols)
                self.spots[i].append(spot)

    def get_spots(self):
        return self.spots

    def draw_grid_line(self):
        for i in range(self.rows):
            pygame.draw.line(self.win, GREY, (0, i*self.row_interval), (self.width, i*self.row_interval))
        for j in range(self.cols):
            pygame.draw.line(self.win, GREY, (j*self.col_interval, 0), (j*self.col_interval, self.height))
