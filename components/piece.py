import pygame.draw

from components.options import *


class Piece:
    def __init__(self):
        pass
        #self.cell = cell

    def get_draw_pos(self, cell):
        pass

    @staticmethod
    def draw_piece(screen, x, y):
        pygame.draw.circle(screen, PIECE_OUTLINE_COLOR, (x, y), PIECE_RADIUS + PIECE_OUTLINE)
        pygame.draw.circle(screen, PIECE_COLOR, (x, y), PIECE_RADIUS)
