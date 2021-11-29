import pygame.draw

from components.options import *


class Piece:
    def __init__(self, cell):
        self.cell = cell
        self.x = 20
        self.y = 20

    def get_draw_pos(self,cell):
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, PIECE_OUTLINE_COLOR, (self.x, self.y), PIECE_RADIUS + PIECE_OUTLINE)
        pygame.draw.circle(screen, PIECE_COLOR, (self.x, self.y), PIECE_RADIUS)
