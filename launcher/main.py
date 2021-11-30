from math import sqrt
from components.board import *
from components.graphics import draw_text, draw_score
from components.initialization import init_game, init_board
from components.options import *
from logic.logic import Logic

if __name__ == '__main__':
    window = init_game()
    board = init_board(window)
    logic = Logic(board)

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
                draw_text(window, SCORE_TEXT_COLOR,str(i), TEMP_TEXT)

            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(board)
                logic.movement_logic()

        board.draw_board()
        draw_score(window, board)
        pygame.display.update()
    pygame.quit()
