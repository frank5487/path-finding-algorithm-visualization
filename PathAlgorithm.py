from queue import PriorityQueue, Queue

import pygame


class PathAlgorithm:
    def __init__(self, draw, spots, start, end):
        self.spots = spots
        self.start = start
        self.end = end
        self.draw = draw

    def heuristic(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (x1-x2)**2 + (y1-y2)**2

    def get_distance(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return (x1-x2)**2 + (y1-y2)**2
    
    def reconstruct_path(self, came_from, current):
        cnt = 0
        while current in came_from:
            cnt += 1
            current = came_from[current]
            if current == self.start:
                break
            current.set_path()
            self.draw()
        print(cnt)

    def a_star(self):
        count = 0
        q = PriorityQueue()
        q.put((0, count, self.start))
        open_dict = {self.start}
        came_from = {}
        g = {spot: float("inf") for row in self.spots for spot in row}
        g[self.start] = 0
        f = {spot: float("inf") for row in self.spots for spot in row}
        f[self.start] = self.heuristic(self.start.get_pos(), self.end.get_pos())
        
        while not q.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            current = q.get()[2]
            if current == self.end:
                self.reconstruct_path(came_from, self.end)
                self.end.set_end()
                print(count)
                return True
            
            for neighbor in current.neighbors:
                next_g = g[current] + self.get_distance(neighbor.get_pos(), current.get_pos())
                # next_g = g[current] + 1
                if next_g < g[neighbor]:
                    came_from[neighbor] = current
                    g[neighbor] = next_g
                    f[neighbor] = g[neighbor] + self.heuristic(neighbor.get_pos(), self.end.get_pos())
                    if neighbor not in open_dict:
                        count += 1
                        q.put((f[neighbor], count, neighbor))
                        open_dict.add(neighbor)
                        neighbor.set_open()

            if current != self.start:
                current.set_closed()

            self.draw()

        return False

    def dijkstra(self):
        count = 0
        q = PriorityQueue()
        q.put((0, count, self.start))
        open_dict = {self.start}
        g = {spot: float("inf") for row in self.spots for spot in row}
        g[self.start] = 0
        came_from = {}

        while not q.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            current = q.get()[2]
            if current == self.end:
                self.reconstruct_path(came_from, current)
                self.end.set_end()
                print(count)
                return True
            
            for neighbor in current.neighbors:
                next_g = g[current] + self.get_distance(neighbor.get_pos(), current.get_pos())
                if next_g < g[neighbor]:
                    came_from[neighbor] = current
                    g[neighbor] = next_g
                    if neighbor not in open_dict:
                        count += 1
                        q.put((g[neighbor], count, neighbor))
                        open_dict.add(neighbor)
                        neighbor.set_open()

            if current != self.start:
                current.set_closed()

            self.draw()

        return False

    
    def bfs(self):
        count = 0
        q = Queue()
        q.put((count, self.start))
        open_dict = {self.start}
        came_from = {}

        while not q.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
            current = q.get()[1]
            if current == self.end:
                self.reconstruct_path(came_from, current)
                self.end.set_end()
                print(count)
                return True
            
            for neighbor in current.neighbors:
                if neighbor not in open_dict:
                    came_from[neighbor] = current
                    count += 1
                    q.put((count, neighbor))
                    open_dict.add(neighbor)
                    neighbor.set_open()

            if current != self.start:
                current.set_closed()

            self.draw()

        return False