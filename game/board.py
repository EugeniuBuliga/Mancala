import pygame
from .options import *


class Board:
    def __init__(self):
        self.board = []
        self.selected_region = None

    def draw_regions(self, screen):
        border = HEIGHT / 4
        cell_width = WIDTH / 9
        cell_height = HEIGHT / 4
        storage_width = WIDTH / 9 * 1.5
        storage_height = HEIGHT / 2

        left_storage_b = (0, border, storage_width, storage_height)
        right_storage_b = (WIDTH - storage_width, border, storage_width, storage_height)
        left_storage = (0 + 1, border + 1, storage_width - 2, storage_height - 2)
        right_storage = (WIDTH - storage_width + 1, border + 1, storage_width - 2, storage_height - 2)

        pygame.draw.rect(screen, BORDER_COLOR, left_storage_b)
        pygame.draw.rect(screen, BORDER_COLOR, right_storage_b)
        pygame.draw.rect(screen, CELL_COLOR, left_storage)
        pygame.draw.rect(screen, CELL_COLOR, right_storage)

        upper_cells = []
        upper_cells_borders = []
        for i in range(0, 6):
            upper_cells.append((storage_width + cell_width * i, border, cell_width, cell_height))
            upper_cells_borders.append(
                (storage_width + cell_width * i + 1, border + 1, cell_width - 2, cell_height - 2))

        for c in upper_cells:
            pygame.draw.rect(screen, BORDER_COLOR, c)

        for d in upper_cells_borders:
            pygame.draw.rect(screen, CELL_COLOR, d)

        lower_cells = []
        lower_cells_borders = []
        for i in range(0, 6):
            lower_cells.append((storage_width + cell_width * i, border + cell_height, cell_width, cell_height))
            lower_cells_borders.append(
                (storage_width + cell_width * i + 1, border + cell_height + 1, cell_width - 2, cell_height - 2))

        for e in lower_cells:
            pygame.draw.rect(screen, BORDER_COLOR, e)

        for f in lower_cells_borders:
            pygame.draw.rect(screen, CELL_COLOR, f)
