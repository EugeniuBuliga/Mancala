import pygame


class Logic:
    def __init__(self, board):
        self.board = board
        self.active_player = board.players[0]
        self.move_made = False

    def movement_logic(self):
        for i in [2, 3]:
            for j in range(0, 6):
                (x, y) = pygame.mouse.get_pos()
                if self.board.cells[i][j].is_on_cell(x, y):
                    if self.is_players_cell(self.board.cells[i][j]):
                        self.make_move(i, j)
                        self.move_made = True

    @staticmethod
    def next_in_order(i, j):
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

    def make_move(self, i, j):
        actual_i = i
        actual_j = j
        while self.board.cells[i][j].inventory:
            next1, next2 = self.next_in_order(actual_i, actual_j)
            actual_i, actual_j = next1, next2
            self.add_piece_to(actual_i, actual_j)
            self.board.cells[i][j].remove_piece()

    def add_piece_to(self, n1, n2):
        if n2 != -9:
            self.board.cells[n1][n2].add_n_pieces(1)
        else:
            self.board.cells[n1].add_n_pieces(1)

    def next_player(self):
        if self.active_player == self.board.players[0]:
            self.active_player = self.board.players[1]
        else:
            self.active_player = self.board.players[0]

    def is_players_cell(self, cell):
        if cell in self.active_player.allowed:
            return True
        else:
            return False
