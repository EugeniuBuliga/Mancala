import sys, pygame
from math import sqrt, log, exp

from components.board import *
from components.graphics import set_text
from components.initialization import init_game
from components.piece import Piece
from options import *

if __name__ == '__main__':
    window = init_game()

    clock = pygame.time.Clock()
    run = True
    board = Board()
    board.init_board(window)
    board.add_pieces()

    i = 0
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                i += 1 + int(sqrt(i)) * 200000
                pygame.draw.rect(window, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
                text = set_text(str(i), (255, 255, 255), (WIDTH / 2, HEIGHT / 8))
                window.blit(text[0], text[1])
                board.draw_board()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        pygame.display.update()

    pygame.quit()
