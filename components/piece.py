import pygame.draw

from components.options import *


class Piece:
    def __init__(self, screen):
        self.screen = screen

    def draw_piece(self, x, y):
        """
        Draw the piece on given coordinates.
        :param x: coords x
        :param y: coords y
        """
        pygame.draw.circle(self.screen, PIECE_OUTLINE_COLOR, (x, y), PIECE_RADIUS + PIECE_OUTLINE)
        pygame.draw.circle(self.screen, PIECE_COLOR, (x, y), PIECE_RADIUS)
