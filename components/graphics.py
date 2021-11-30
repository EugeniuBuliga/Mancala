import pygame

from components.options import *


# def draw_text_old(screen, text):
#     text_obj = set_text(text, (255, 255, 255), (WIDTH / 2, HEIGHT / 8))
#     screen.blit(text_obj[0], text_obj[1])


def draw_text(screen, color, text, center, font='freesansbold.ttf'):
    """
    Write a text on given coordinates.

    :param screen:
    :param font:
    :param text: the text to write
    :param color: color of the text
    :param center: coords of center
    :return: text, text_rect
    """

    font = pygame.font.Font(font, 30)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = center

    screen.blit(text, text_rect)


def draw_score(screen, board):
    score_player1 = str(len(board.cells[0].inventory))
    score_player2 = str(len(board.cells[1].inventory))
    # print(score_player1,":",score_player2)
    draw_text(screen, SCORE_TEXT_COLOR, score_player1, SCORE1)
    draw_text(screen, SCORE_TEXT_COLOR, score_player2, SCORE2)
