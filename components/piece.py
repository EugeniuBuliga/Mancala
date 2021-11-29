import pygame.draw

from components.options import *


class Piece:
    def __init__(self):
        #self.cell = cell
        self.stored = False
        self.x = WIDTH/9 - 10
        self.y = HEIGHT / 2


    def draw(self, screen):
        piece_radius = int(WIDTH/25)
        outline = 3
        pygame.draw.circle(screen,(0,0,0), (self.x,self.y), piece_radius+outline)
        pygame.draw.circle(screen,PIECE_COLOR, (self.x,self.y), piece_radius)

