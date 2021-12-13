import pygame
from time import sleep
from components.board import Board
from components.cell import Cell
from components.options import SLEEP_ANIMATION_TIME
from logic.ailogic import Ai
from logic.player import Player


class Logic:
    def __init__(self, board: Board):
        self.board = board
        self.active_player = board.players[0]
        self.move_made = False
        self.ended_move_on_piece = False
        self.hint1 = self.active_player.name + "'s turn"
        self.hint2 = ""
        self.last_cell = board.cells[0]
        self.ended = False

        self.opponent_is_ai = False
        self.ai = None

    @staticmethod
    def transfer_pieces(cell1: Cell, cell2: Cell) -> bool:
        """
        Transfer the pieces from a cell, to another.

        :param cell1: from
        :param cell2: to
        :return: True if transfer took place.
        """
        if cell1.inventory:
            while cell1.inventory:
                cell2.add_n_pieces(1)
                cell1.remove_piece()
            return True
        else:
            return False

    @staticmethod
    def next_in_order(i: int, j: int) -> (int, int):
        """
        Gives the next cell in order of the game.

        :param i: i position in cells list (2 = up, 3 = down)
        :param j: j position in row
        :return: The next cells coordinates in cells list.
        """
        if i == 3:
            if j + 1 <= 5:
                return i, j + 1
            else:
                return 1, -9
        elif i == 2:
            if j - 1 >= 0:
                return i, j - 1
            else:
                return 0, -9
        elif i == 0:
            return 3, 0
        elif i == 1:
            return 2, 5

    def set_ai_opponent(self):
        """
        Initializes the AI components.
        """

        self.opponent_is_ai = True
        self.ai = Ai(self.board)

    def opposite_cell(self, cell: Cell) -> Cell:
        """
        Get the cell from the opposite row.

        :param cell: the cell whose opposite is needed.
        :return: cell with the same position, but from the other row.
        """
        if cell.cell_type == "upper":
            opposite = self.board.cells[3][int(cell.order)]
        else:
            opposite = self.board.cells[2][int(cell.order)]
        return opposite

    def get_winner(self) -> [Player, str]:
        """
        Get the winner(s) of the game.

        :return: a player if won, "both" if game ended in a draw.
        """
        if len(self.board.players[0].storage.inventory) > len(self.board.players[1].storage.inventory):
            return self.board.players[0]
        elif len(self.board.players[0].storage.inventory) < len(self.board.players[1].storage.inventory):
            return self.board.players[1]
        else:
            return "both"

    def check_win_state(self, i: int):
        """
        Checks if the game was won and sends the print message to 'hint2'.

        :param i: row
        """
        empty_nr = 0
        for j in range(0, 6):
            if self.board.cells[i][j].is_empty():
                empty_nr += 1

        if empty_nr == 6:
            winner = self.get_winner()
            if winner != "both":
                self.hint2 = "Game ended: " + winner.name + " won!"
            else:
                self.hint2 = "Game ended: " + "Ended in a draw!"
            self.ended = True

    def is_players_cell(self, cell: Cell) -> bool:
        """
        Determines whether the cell belongs to the active_player or not.

        :param cell: the cell whose appartenance needs to be checked.
        :return: True if active_player can click it, False if not.
        """
        if cell in self.active_player.allowed:
            return True
        else:
            return False

    def add_piece_to(self, n1: int, n2: int):
        """
        Ads pieces to the cell, according to its type (derived from the two input parameters)

        :param n1: position in cells list
        :param n2: position in cells list (if ==-9, then it's a storage, not a cell, so it's not taken into account)
        """
        if n2 != -9:
            self.board.cells[n1][n2].add_n_pieces(1)
        else:
            self.board.cells[n1].add_n_pieces(1)

    def make_move(self, i: int, j: int):
        """
        Performs movement of the pieces on the board, on the cell specified.

        :param i: i position in cells list (2 = up, 3 = down)
        :param j: j position in row
        """
        actual_i = i
        actual_j = j
        while self.board.cells[i][j].inventory:
            next1, next2 = self.next_in_order(actual_i, actual_j)
            if next1 != self.active_player.get_storage() and next2 == -9:
                next1, next2 = self.next_in_order(next1, next2)
            actual_i, actual_j = next1, next2
            self.add_piece_to(actual_i, actual_j)

            sleep(SLEEP_ANIMATION_TIME)
            self.board.draw_board()
            pygame.display.update()

            self.board.cells[i][j].remove_piece()
            self.move_made = True
        if actual_i == 0 == self.active_player.get_storage() or actual_i == 1 == self.active_player.get_storage():
            self.ended_move_on_piece = True
            self.last_cell = self.board.cells[actual_i]
        elif actual_i == 0 or actual_i == 1:
            self.last_cell = self.board.cells[actual_i]
        else:
            self.last_cell = self.board.cells[actual_i][actual_j]

    def capture(self) -> bool:
        """
        Capture enemy pieces.

        :return: True if pieces captured.
        """
        if len(self.last_cell.inventory) == 1 and not self.last_cell.is_storage:
            if self.opposite_cell(self.last_cell) not in self.active_player.allowed:
                if self.transfer_pieces(self.opposite_cell(self.last_cell), self.active_player.storage):
                    self.hint2 = self.active_player.name + " captured opponent's pieces"
                    return True
        return False

    def movement_logic(self):
        """
        Keeps track of all the actions regarding gameplay.
        """
        for i in [2, 3]:
            for j in range(0, 6):

                if not self.opponent_is_ai:
                    (x, y) = pygame.mouse.get_pos()
                elif self.opponent_is_ai and self.active_player.get_storage() == 1:
                    (x, y) = pygame.mouse.get_pos()
                else:
                    (x, y) = self.ai.get_ai_move()

                if self.board.cells[i][j].is_on_cell(x, y):
                    if self.is_players_cell(self.board.cells[i][j]):
                        self.make_move(i, j)
                        if not self.capture():
                            self.hint2 = ""
                self.board.cells[i][j].clear_selection()
                self.check_win_state(i)

    def next_player(self):
        """
        Determines who is the next player to make a move.
        """
        if not self.ended_move_on_piece:
            if self.active_player == self.board.players[0]:
                self.active_player = self.board.players[1]
            else:
                self.active_player = self.board.players[0]
            self.hint1 = self.active_player.name + "'s turn"
        else:
            self.ended_move_on_piece = False
            if self.opponent_is_ai:
                self.ai.allow_move()
