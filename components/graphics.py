import pygame
from pygame.surface import Surface
from components.board import Board
from components.options import *
from logic.logic import Logic


def draw_text(screen: Surface, color: (int, int, int), text: str, center: (int, int), font=FONT):
    """
    Write a text on given coordinates.

    :param screen: Screen open which to draw the text.
    :param font: Font used for text.
    :param text: the text to write
    :param color: color of the text
    :param center: coords of center
    """

    font = pygame.font.Font(font, 30)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = center
    screen.blit(text, text_rect)


def draw_score(screen: Surface, board: Board):
    """
    Draws the score of both players on proper place on the screen.

    :param screen: Screen open which to draw the text.
    :param board: Game board, to extract the score from.
    """
    score_player1 = str(len(board.cells[0].inventory))
    score_player2 = str(len(board.cells[1].inventory))
    draw_text(screen, SCORE_TEXT_COLOR, score_player1 + ":" + score_player2, SCORE_POS)


def draw_players(screen: Surface, board: Board):
    """
    Draws players' names on screen.

    :param screen: Screen open which to draw the text.
    :param board: Game board, to extract the players from.
    """
    draw_text(screen, SCORE_TEXT_COLOR, board.players[1].name, PLAYER1_POS)
    draw_text(screen, SCORE_TEXT_COLOR, board.players[0].name, PLAYER2_POS)


def draw_hint(screen: Surface, logic: Logic):
    """
    Draw hints regarding gameplay in the bottom of the screen.

    :param screen: Screen open which to draw the text.
    :param logic: Game logic, that controls flow of the game.
    """
    draw_text(screen, SCORE_TEXT_COLOR, logic.hint1, HINT1_POS)
    draw_text(screen, SCORE_TEXT_COLOR, logic.hint2, HINT2_POS)
