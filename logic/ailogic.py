from components.options import *
import random as rand


class Ai:
    def __init__(self, board):
        self.board = board
        self.available_moves = self.update_ai_moves()
        self.move_allowed = False
        self.move = rand.choice(self.available_moves)

    def allow_move(self):
        self.move_allowed = True

    def update_ai_moves(self):
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


    def clear_moves(self):
        if hasattr(self, 'available_moves'):
            self.available_moves.clear()

    def get_ai_move(self):
        if self.move_allowed:
            self.update_ai_moves()
            self.move = rand.choice(self.available_moves)
            print(self.move)
            self.move_allowed = False
            return self.move
        else:
            return self.move
