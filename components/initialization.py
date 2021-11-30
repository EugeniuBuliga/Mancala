import pygame

from components.board import Board
from components.options import *


def init_game():
    """
    Initializes the main components of the app.
    :return: display window object
    """
    pygame.init()
    size = WIDTH, HEIGHT
    window = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Mancala")

    return window


def init_board(screen):
    """
    Initializes the board and its components.
    :param screen:
    :return:
    """
    board = Board(screen)
    board.init_board()
    board.init_pieces()
    return board
