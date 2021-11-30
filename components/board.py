from logic.player import Player
from .cell import Cell
from .options import *


class Board:
    def __init__(self, screen):
        self.screen = screen

        self.cells = []
        self.selected_region = None
        self.players = []

    def __str__(self):
        message = str(self.cells[0]) + str(self.cells[1]) + "\n["
        for cell in self.cells[2]:
            message += str(cell)
        message += "],\n["
        for cell in self.cells[3]:
            message += str(cell)
        message += "]"
        return message

    def add_default_players(self):
        """
        Initializes players.
        """
        player1 = Player(self, "Player1", "down")
        self.players.append(player1)
        player2 = Player(self, "Player2", "up")
        self.players.append(player2)

    def init_board(self):
        """
        Initializes main Board class components.
        """
        storage1 = Cell(self.screen, "left", True)
        self.cells.append(storage1)
        storage2 = Cell(self.screen, "right", True)
        self.cells.append(storage2)

        upper_row = []
        for i in range(6):
            upper_row.append(Cell(self.screen, "upper", False, str(i)))
        self.cells.append(upper_row)

        lower_row = []
        for i in range(6):
            lower_row.append(Cell(self.screen, "lower", False, str(i)))
        self.cells.append(lower_row)

        self.add_default_players()

    def draw_board(self):
        """
        Draws all board elements on the screen.
        """
        # draw storages
        self.cells[0].draw_cell()
        self.cells[1].draw_cell()

        # draw upper row of cells
        i = 0
        for cell in self.cells[2]:
            cell.draw_cell()
            i += 1

        # draw lower row of cells
        i = 0
        for cell in self.cells[3]:
            cell.draw_cell()
            i += 1

        # draw pieces in bot rows of cells
        for i in [2, 3]:
            for cell in self.cells[i]:
                cell.draw_inventory()

        # draw pieces in storages
        for i in [0, 1]:
            self.cells[i].draw_inventory()

    def init_pieces(self):
        """
        Draw initial number of pieces on the board.
        """
        for i in [2, 3]:
            for j in range(0, 6):
                self.cells[i][j].add_n_pieces(INITIAL_PIECES_NR)
