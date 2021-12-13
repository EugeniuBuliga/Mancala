from components.board import Board
from components.options import *
import random as rand


class Ai:
    def __init__(self, board: Board):
        self.board = board
        self.available_moves = self.update_ai_moves()
        self.move_allowed = False
        self.move = rand.choice(self.available_moves)

    def allow_move(self):
        """
        Allows AI to make next move.
        """
        self.move_allowed = True

    def clear_moves(self):
        """
        Removes all the moves from the available_moves attribute, if it is not empty.
        """
        if hasattr(self, 'available_moves'):
            self.available_moves.clear()

    def update_ai_moves(self) -> list:
        """
        Updates the list of available moves, based on the cells that are not empty.

        :return: available_moves list attribute, if it has not been initialized.
        """
        self.clear_moves()
        available_moves = []
        for cell in self.board.cells[2]:
            if not cell.is_empty():
                x = cell.x + CELL_WIDTH / 2
                y = cell.y + CELL_HEIGHT / 2
                available_moves.append([x, y])
        if not hasattr(self, 'available_moves'):
            return available_moves
        else:
            self.available_moves = available_moves
            self.move_allowed = True

    def get_ai_move(self) -> (int, int):
        """
        Get AI's next move if movement allowed, or the already chosen move, if movement restricted.

        :return: AI's next move.
        """
        if self.move_allowed:
            self.update_ai_moves()
            if self.available_moves:
                self.move = rand.choice(self.available_moves)
            self.move_allowed = False
            return self.move
        else:
            return self.move
