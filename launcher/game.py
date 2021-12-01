import pygame
from components.board import *
from components.graphics import draw_score, draw_players, draw_hint
from components.initialization import init_game, init_board
from components.options import *
from logic.logic import Logic


def play_game(opponent):
    """
    Main game function.

    :param opponent: type of opponent ('ai' or 'pvp')
    """

    window = init_game()
    board = init_board(window)
    logic = Logic(board)
    if opponent == "ai":
        logic.set_ai_opponent()

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEMOTION:
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(board)
                logic.movement_logic()
                if logic.move_made:
                    logic.next_player()
                    logic.move_made = False

                if logic.opponent_is_ai:
                    logic.ai.update_ai_moves()

        # graphics (screen updates)
        pygame.draw.rect(window, BACKGROUND_COLOR, (0, 0, WIDTH, HEIGHT))
        board.draw_board()
        draw_players(window, board)
        draw_score(window, board)
        draw_hint(window, logic)
        pygame.display.update()
    pygame.quit()
