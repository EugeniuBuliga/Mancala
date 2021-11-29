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

    def init_board(self, screen):
        """
        Initializes main Board class components.
        """
        storage1 = Cell(screen, True, "left")
        self.cells.append(storage1)

        storage2 = Cell(screen, True, "right")
        self.cells.append(storage2)

        upper_row = []
        for i in range(6):
            upper_row.append(Cell(screen, False, "upper", str(i)))
        self.cells.append(upper_row)

        lower_row = []
        for i in range(6):
            lower_row.append(Cell(screen, False, "lower", str(i)))
        self.cells.append(lower_row)

    def draw_board(self):
        """
        Draws all board elements on the screen.
        :param screen: The screen upon which to draw.
        """
        self.cells[0].draw_cell()
        self.cells[1].draw_cell()

        i = 0
        for cell in self.cells[2]:
            cell.draw_cell()
            i += 1

        i = 0
        for cell in self.cells[3]:
            cell.draw_cell()
            i += 1

        for i in [2, 3]:
            for cell in self.cells[i]:
                cell.draw_pieces()

        for i in [0, 1]:
            self.cells[i].draw_pieces()

    def add_pieces(self):
        for i in [2, 3]:
            for j in range(0, 6):
                self.cells[i][j].add_pieces_forced(4)
