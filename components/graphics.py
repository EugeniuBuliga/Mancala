import pygame

from components.options import *


def set_text(string, color, *center):
    """
    Write a text on given coordinates.

    :param string: the text to write
    :param color: color of the text
    :param center: coords of center
    :return: surface, rect
    """

    font = pygame.font.Font('freesansbold.ttf', 30)
    text = font.render(string, True, color)
    text_rect = text.get_rect()
    text_rect.center = center
    return text, text_rect
