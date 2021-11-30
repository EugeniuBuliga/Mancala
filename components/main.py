import sys, pygame
from math import sqrt, log, exp

from components.board import *
from components.graphics import set_text, draw_text
from components.initialization import init_game, init_board
from components.piece import Piece
from options import *

if __name__ == '__main__':
    window = init_game()
    board = init_board(window)

    clock = pygame.time.Clock()
    run = True

    i = 0
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                i += 1 + int(sqrt(i)) * 200000
                pygame.draw.rect(window, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
                draw_text(window, str(i))

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(board)
                for i in [2, 3]:
                    for j in range(0, 6):
                        (x, y) = pygame.mouse.get_pos()
                        if board.cells[i][j].is_on_cell(x, y):
                            board.cells[i][j].remove_piece()
                            if i == 3:
                                if j < 5:
                                    board.cells[i][j + 1].add_n_pieces(1)
                                else:
                                    board.cells[1].add_n_pieces(1)
                            else:
                                if j > 0:
                                    board.cells[i][j - 1].add_n_pieces(1)
                                else:
                                    board.cells[0].add_n_pieces(1)

        board.draw_board()
        pygame.display.update()

    pygame.quit()
