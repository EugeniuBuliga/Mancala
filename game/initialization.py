import pygame
from game.options import *


def init_game():
    """
    Initializes the main game components.
    :return: display window object
    """
    pygame.init()
    size = WIDTH, HEIGHT
    window = pygame.display.set_mode(size)
    pygame.display.set_caption("Mancala")

    return window
