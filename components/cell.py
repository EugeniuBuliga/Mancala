import pygame
from pygame.surface import Surface
from components.options import *
from components.piece import Piece


class Cell:
    def __init__(self, screen: Surface, cell_type: str, is_storage="False", order="1"):
        self.screen = screen
        self.cell_type = cell_type
        self.is_storage = is_storage
        self.order = order

        self.is_selected = False
        self.inventory = []

        self.x, self.y = self.set_x_and_y()
        self.border_color, self.cell_border_width = self.set_colors_and_borders()

    def __str__(self) -> str:
        func1 = (lambda x: "Storage" if x else "Cell")
        func2 = (lambda x: self.order if not x else "S")
        message = func1(self.is_storage) + "<" + self.cell_type + "-" + func2(self.is_storage) + ">"
        return message

    def __repr__(self) -> str:
        return self.__str__()

    def set_x_and_y(self) -> (int, int):
        """
        Sets cells x and y coordinates based on its type.

        :return: x and y coordinates of the cell
        """

        if self.is_storage:
            y = BORDER_UPPER
            if self.cell_type == "left":
                x = BORDER_SIDE
            else:
                x = WIDTH - STORAGE_WIDTH - BORDER_SIDE
        else:
            x = CELL_PADDING + CELL_WIDTH * int(self.order)
            if self.cell_type == "upper":
                y = BORDER_UPPER
            else:
                y = BORDER_UPPER + CELL_HEIGHT
        return x, y

    def set_colors_and_borders(self) -> ((int, int, int), int):
        """
        Set the colors and thickness of the borders, based on the fact that cell is selected or not.

        :return: border_color and cell_border_color
        """

        if self.is_selected:
            border_color = SELECTED_BORDER_COLOR
            cell_border_width = CELL_BORDER_WIDTH * 3
        else:
            border_color = BORDER_COLOR
            cell_border_width = CELL_BORDER_WIDTH
        return border_color, cell_border_width

    def draw_cell(self):
        """
        Draw a specific cell or storage on the appropriate place on the screen.
        """

        self.border_color, self.cell_border_width = self.set_colors_and_borders()

        if not self.is_storage:
            # draw the border rectangle
            border = (self.x,
                      self.y,
                      CELL_WIDTH,
                      CELL_HEIGHT)

            pygame.draw.rect(self.screen, self.border_color, border)

            # draw the rectangle itself
            cell = (self.x + self.cell_border_width,
                    self.y + self.cell_border_width,
                    CELL_WIDTH - 2 * self.cell_border_width,
                    CELL_HEIGHT - 2 * self.cell_border_width)

            pygame.draw.rect(self.screen, CELL_COLOR, cell)

        else:
            # draw the border rectangle
            border = (self.x,
                      BORDER_UPPER,
                      STORAGE_WIDTH,
                      STORAGE_HEIGHT)

            pygame.draw.rect(self.screen, BORDER_COLOR, border)

            # draw the rectangle itself
            cell = (self.x + CELL_BORDER_WIDTH,
                    BORDER_UPPER + CELL_BORDER_WIDTH,
                    STORAGE_WIDTH - 2 * CELL_BORDER_WIDTH,
                    STORAGE_HEIGHT - 2 * CELL_BORDER_WIDTH)

            pygame.draw.rect(self.screen, CELL_COLOR, cell)

    def remove_piece(self) -> bool:
        """
        Removes one piece from this cell's inventory.

        :return: True if the function really did remove a piece. False if removing a piece is impossible (no more pieces
         on the cell).
        """
        if self.inventory:
            self.inventory.pop()
            return True
        else:
            return False

    def draw_inventory(self):
        """
        Draws all pieces in a cell's inventory.
        """
        x = self.x
        pad = CELL_WIDTH / 4
        y = self.y
        i = 1
        j = 1
        for piece in self.inventory:
            piece.draw_piece(x + pad * i, y + pad * j)

            if i < 3 and not self.is_storage:
                i += 1
            elif i < 5 and self.is_storage:
                i += 1
            else:
                i = 1
                j += 1

    def add_n_pieces(self, n: int):
        """
        Adds to a cell's inventory the n amount of pieces.

        :param n: Amount of pieces.
        """
        for i in range(n):
            piece = Piece(self.screen)
            self.inventory.append(piece)

    def is_on_cell(self, x: int, y: int) -> bool:
        """
        Checks if coordinates are inside a specific cell's borders.

        :param x: coords x
        :param y: coords y
        :return: True/False
        """
        if self.x < x < self.x + CELL_WIDTH and self.y < y < self.y + CELL_HEIGHT:
            self.is_selected = True
            return True
        else:
            self.is_selected = False
            return False

    def clear_selection(self):
        """
        Unselect selected cell. (removes selected border)
        """
        self.is_selected = False

    def is_empty(self) -> bool:
        """
        Check if cell has no pieces.

        :return: True if there are no pieces. False if there still is something on the cell.
        """
        if self.inventory:
            return False
        else:
            return True
