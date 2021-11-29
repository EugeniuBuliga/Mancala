import pygame
from components.options import *


class Cell:
    def __init__(self, is_storage, cell_type):
        self.is_storage = is_storage
        self.cell_type = cell_type
        self.contains = []

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

    def draw_cell(self, screen, order="1"):
        """
        Draw a specific cell or storage on the right place on the screen.

        :param screen: The screen upon which to draw.
        :param order: Order of the cell.
        :return:
        """

        order = int(order)

        # determine whether cell is a normal cell or a storage
        if not self.is_storage:
            # set row of the cell
            if self.cell_type == "upper":
                upper_padding = BORDER_UPPER
            else:
                upper_padding = BORDER_UPPER + CELL_HEIGHT

            # draw the border rectangle
            border = (CELL_PADDING + CELL_WIDTH * order,
                      upper_padding,
                      CELL_WIDTH,
                      CELL_HEIGHT)

            pygame.draw.rect(screen, BORDER_COLOR, border)

            # draw the rectangle itself
            cell = (CELL_PADDING + CELL_WIDTH * order + CELL_BORDER_WIDTH,
                    upper_padding + CELL_BORDER_WIDTH,
                    CELL_WIDTH - 2 * CELL_BORDER_WIDTH,
                    CELL_HEIGHT - 2 * CELL_BORDER_WIDTH)

            pygame.draw.rect(screen, CELL_COLOR, cell)
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

            pygame.draw.rect(screen, BORDER_COLOR, border)

            # draw the rectangle itself

            cell = (padding + CELL_BORDER_WIDTH,
                    BORDER_UPPER + CELL_BORDER_WIDTH,
                    STORAGE_WIDTH - 2 * CELL_BORDER_WIDTH,
                    STORAGE_HEIGHT - 2 * CELL_BORDER_WIDTH)

            pygame.draw.rect(screen, CELL_COLOR, cell)
