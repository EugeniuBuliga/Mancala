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

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in [2, 3]:
                    for j in range(0, 6):
                        (x, y) = pygame.mouse.get_pos()
                        if board.cells[i][j].is_mouse_on_piece(x, y):
                            board.cells[i][j].remove_piece()
                            if i == 3:
                                if j < 5:
                                    board.cells[i][j + 1].add_pieces_forced(1)
                                else:
                                    board.cells[1].add_pieces_forced(1)
                            else:
                                if j > 0:
                                    board.cells[i][j - 1].add_pieces_forced(1)
                                else:
                                    board.cells[0].add_pieces_forced(1)

        board.draw_board()
        pygame.display.update()

    pygame.quit()
