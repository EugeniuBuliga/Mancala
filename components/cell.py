import pygame
from components.options import *
from components.piece import Piece


class Cell:
    def __init__(self, screen, is_storage, cell_type, order="1"):
        self.is_storage = is_storage
        self.cell_type = cell_type
        self.order = order
        self.screen = screen
        self.contains = []
        self.x = CELL_PADDING + CELL_WIDTH * int(order)
        if self.cell_type == "upper":
            self.y = BORDER_UPPER
        else:
            self.y = BORDER_UPPER + CELL_HEIGHT

    def __str__(self):
        # ################try lambda expression here later
        # return (lambda x: "Storage" if self.is_storage else "Cell") + " of type " + self.cell_type
        message = ""
        if self.is_storage:
            message += "Storage"
        else:
            message += "Cell"
        message += "<" + self.cell_type + ">,"
        return message

    def draw_cell(self):
        """
        Draw a specific cell or storage on the right place on the screen.
        """

        # determine whether cell is a normal cell or a storage
        if not self.is_storage:

            # draw the border rectangle
            border = (self.x,
                      self.y,
                      CELL_WIDTH,
                      CELL_HEIGHT)

            pygame.draw.rect(self.screen, BORDER_COLOR, border)

            # draw the rectangle itself
            cell = (self.x + CELL_BORDER_WIDTH,
                    self.y + CELL_BORDER_WIDTH,
                    CELL_WIDTH - 2 * CELL_BORDER_WIDTH,
                    CELL_HEIGHT - 2 * CELL_BORDER_WIDTH)

            pygame.draw.rect(self.screen, CELL_COLOR, cell)
        else:
            # set position of the storage
            if self.cell_type == "left":
                padding = BORDER_SIDE
            else:
                padding = WIDTH - STORAGE_WIDTH - BORDER_SIDE

            # draw the border rectangle
            border = (padding,
                      BORDER_UPPER,
                      STORAGE_WIDTH,
                      STORAGE_HEIGHT)

            pygame.draw.rect(self.screen, BORDER_COLOR, border)

            # draw the rectangle itself

            cell = (padding + CELL_BORDER_WIDTH,
                    BORDER_UPPER + CELL_BORDER_WIDTH,
                    STORAGE_WIDTH - 2 * CELL_BORDER_WIDTH,
                    STORAGE_HEIGHT - 2 * CELL_BORDER_WIDTH)

            pygame.draw.rect(self.screen, CELL_COLOR, cell)

    def add_piece(self, piece):
        self.contains.append(piece)

    def remove_piece(self, piece):
        self.contains.remove(piece)

    def draw_pieces(self):
        x = self.x
        pad = CELL_WIDTH / 4
        y = self.y
        i = 1
        j = 1
        for piece in self.contains:
            piece.draw_piece(self.screen, x + pad * i, y + pad * j)

            if i < 3:
                i += 1
            else:
                i = 1
                j += 1

    def add_pieces_forced(self, nr):
        for i in range(nr):
            piece = Piece()
            self.contains.append(piece)
