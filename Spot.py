import pygame
from Constants import *

class Spot:

    def __init__(self, row, col, width, height, total_rows, total_cols):
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.x = col * width
        self.y = row * height
        self.color = WHITE 
        self.neighbors = []

    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE

    def set_closed(self):
        self.color = RED
    
    def set_open(self):
        self.color = GREEN
    
    def set_barrier(self):
        self.color = BLACK
    
    def set_start(self):
        self.color = ORANGE
    
    def set_end(self):
        self.color = TURQUOISE

    def set_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
    def get_pos(self):
        return self.x, self.y
        # return self.row, self.col
    
    def update_neighbors(self, spots):
        self.neighbors = []
        # down
        if self.row+1 < self.total_rows and not spots[self.row+1][self.col].is_barrier():
            self.neighbors.append(spots[self.row+1][self.col])
        # up
        if self.row-1 >= 0 and not spots[self.row-1][self.col].is_barrier():
            self.neighbors.append(spots[self.row-1][self.col])
        # left
        if self.col-1 >= 0 and not spots[self.row][self.col-1].is_barrier():
            self.neighbors.append(spots[self.row][self.col-1])
        # right
        if self.col+1 < self.total_cols and not spots[self.row][self.col+1].is_barrier():
            self.neighbors.append(spots[self.row][self.col+1])
        
    def __lt__(self, others):
        return False


