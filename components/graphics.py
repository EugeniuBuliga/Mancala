import pygame

from components.options import *


def draw_text(screen, color, text, center, font='freesansbold.ttf'):
    """
    Write a text on given coordinates.

    :param screen: Screen open which to draw the text.
    :param font: Font used for text.
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
    """
    Draws the score of both players on proper place on the screen.

    :param screen: Screen open which to draw the text.
    :param board: Game board, to extract the score from.
    """
    score_player1 = str(len(board.cells[0].inventory))
    score_player2 = str(len(board.cells[1].inventory))
    draw_text(screen, SCORE_TEXT_COLOR, score_player1, SCORE1_POS)
    draw_text(screen, SCORE_TEXT_COLOR, score_player2, SCORE2_POS)


def draw_players(screen, board):
    draw_text(screen, SCORE_TEXT_COLOR, board.players[0].name, PLAYER1_POS)
    draw_text(screen, SCORE_TEXT_COLOR, board.players[1].name, PLAYER2_POS)
