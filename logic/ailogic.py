from components.options import *
import random as rand


class Ai:
    def __init__(self, board):
        self.board = board
        self.available_moves = self.ai_set_moves()
        self.actual = -1, -1
        self.move = None

    def ai_set_moves(self):
        available_moves = []
        for cell in self.board.cells[2]:
            if not cell.is_empty():
                x = cell.x + CELL_WIDTH / 2
                y = cell.y + CELL_HEIGHT / 2
                available_moves.append([x, y])
        return available_moves

    def ai_get_move(self, i, j):
        if [i, j] != self.actual:
            self.move = rand.choice(self.available_moves)
            self.actual = [i, j]
            return self.move
        else:
            return self.move
