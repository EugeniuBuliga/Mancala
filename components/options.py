import random as rand

"""
This file contains all constants used in the application.  
"""

# window
WIDTH = 800
HEIGHT = 600

# graphics
FPS = 60

# colors
RAND_COLOR = (rand.randint(1, 255), rand.randint(1, 255), rand.randint(1, 255))
BACKGROUND_COLOR = (0,200,0)
CELL_COLOR = (222, 255, 177)
BORDER_COLOR = (50,30,0)
PIECE_COLOR = (210,105,30)
PIECE_OUTLINE_COLOR = (128,0,0)

# dimensions
CENTER = WIDTH / 2, HEIGHT / 2
BORDER_UPPER = HEIGHT / 4                       # 150
BORDER_SIDE = (WIDTH - 9*int(WIDTH/9))/2        # 4

PIECE_RADIUS = 15
PIECE_OUTLINE = 2

CELL_WIDTH = int(WIDTH / 9)                     # 88
CELL_HEIGHT = HEIGHT / 4                        # 150

STORAGE_WIDTH = CELL_WIDTH * 1.5                # 132
STORAGE_HEIGHT = HEIGHT / 2                     # 300

CELL_PADDING = BORDER_SIDE + STORAGE_WIDTH
CELL_BORDER_WIDTH = 1

