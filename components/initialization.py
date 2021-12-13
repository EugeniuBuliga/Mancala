import pygame
from pygame.surface import Surface

from components.board import Board
from components.options import *


def init_game() -> Surface:
    """
    Initializes the main components of the app.

    :return: Surface
    """
    pygame.init()
    size = WIDTH, HEIGHT
    window = pygame.display.set_mode(size, pygame.RESIZABLE)
    pygame.display.set_caption("Mancala")
    return window


def init_board(screen: Surface) -> Board:
    """
    Initializes the board and its components.

    :param screen: Surface

    :return: Board
    """
    board = Board(screen)
    board.init_board()
    board.init_pieces()
    return board
