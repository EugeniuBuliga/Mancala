import pygame

from .cell import Cell
from .options import *


class Board:
    def __init__(self):
        self.cells = []
        self.selected_region = None

    def __str__(self):
        message = str(self.cells[0]) + str(self.cells[1]) + "["
        for cell in self.cells[2]:
            message += str(cell)
        for cell in self.cells[3]:
            message += str(cell)
        message += "]"
        return message

    def init_board(self):
        """
        Initializes main Board class components.
        """
        storage1 = Cell(True, "left")
        self.cells.append(storage1)

        storage2 = Cell(True, "right")
        self.cells.append(storage2)

        upper_row = []
        for i in range(6):
            upper_row.append(Cell(False, "upper"))
        self.cells.append(upper_row)

        lower_row = []
        for i in range(6):
            lower_row.append(Cell(False, "lower"))
        self.cells.append(lower_row)

    def draw_board(self, screen):
        """
        Draws all board elements on the screen.
        :param screen: The screen upon which to draw.
        """
        self.cells[0].draw_cell(screen)
        self.cells[1].draw_cell(screen)

        i = 0
        for cell in self.cells[2]:
            cell.draw_cell(screen, str(i))
            i += 1

        i = 0
        for cell in self.cells[3]:
            cell.draw_cell(screen, str(i))
            i += 1
