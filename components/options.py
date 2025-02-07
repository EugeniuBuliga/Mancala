import random as rand

"""
This file contains all constants used in the application.  
"""

# window size
WIDTH = 800
HEIGHT = 600

# text font
FONT = 'freesansbold.ttf'

# colors
RAND_COLOR = (rand.randint(1, 255), rand.randint(1, 255), rand.randint(1, 255))
BACKGROUND_COLOR = (0, 200, 0)
CELL_COLOR = (222, 255, 177)
BORDER_COLOR = (50, 30, 0)
SELECTED_BORDER_COLOR = (247, 247, 57)
PIECE_COLOR = (210, 105, 30)
PIECE_OUTLINE_COLOR = (128, 0, 0)
SCORE_TEXT_COLOR = (255, 255, 200)

# graphic elements dimensions and positions
CENTER = WIDTH / 2, HEIGHT / 2
BORDER_UPPER = HEIGHT / 4  # 150
BORDER_SIDE = (WIDTH - 9 * int(WIDTH / 9)) / 2  # 4

PIECE_RADIUS = 15
PIECE_OUTLINE = 2

CELL_WIDTH = int(WIDTH / 9)  # 88
CELL_HEIGHT = HEIGHT / 4  # 150

STORAGE_WIDTH = CELL_WIDTH * 1.5  # 132
STORAGE_HEIGHT = HEIGHT / 2  # 300

CELL_PADDING = BORDER_SIDE + STORAGE_WIDTH
CELL_BORDER_WIDTH = 1

INITIAL_PIECES_NR = 4

# text position
SCORE_POS = WIDTH / 2, HEIGHT / 8
TEMP_TEXT = WIDTH / 2, HEIGHT / 8

PLAYER1_POS = WIDTH / 8, HEIGHT / 8
PLAYER2_POS = WIDTH / 8 * 7, HEIGHT / 8

HINT1_POS = WIDTH / 2, HEIGHT / 8 * 7
HINT2_POS = WIDTH / 2, HEIGHT / 8 * 7.5

# animation parameters
SLEEP_ANIMATION_TIME = 0.2
