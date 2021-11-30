import pygame


class Logic:
    def __init__(self, board):
        self.board = board
        self.active_player = board.players[0]
        self.move_made = False
        self.ended_move_on_piece = False
        self.hint = self.active_player.name + " start the game"

    def movement_logic(self):
        """
        Keeps track of all the actions regarding gameplay.
        """
        for i in [2, 3]:
            for j in range(0, 6):
                (x, y) = pygame.mouse.get_pos()
                if self.board.cells[i][j].is_on_cell(x, y):
                    if self.is_players_cell(self.board.cells[i][j]):
                        self.make_move(i, j)
                        self.move_made = True

    @staticmethod
    def next_in_order(i, j):
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

    def make_move(self, i, j):
        """
        Performs movement of the pieces on the board, on the cell specified.

        :param i: i position in cells list (2 = up, 3 = down)
        :param j: j position in row
        """
        actual_i = i
        actual_j = j
        while self.board.cells[i][j].inventory:
            next1, next2 = self.next_in_order(actual_i, actual_j)
            actual_i, actual_j = next1, next2
            self.add_piece_to(actual_i, actual_j)
            self.board.cells[i][j].remove_piece()
        if actual_i == 0 or actual_i == 1:
            self.ended_move_on_piece = True

    def add_piece_to(self, n1, n2):
        """
        Ads pieces to the cell, according to its type (derived from the two input parameters)

        :param n1: position in cells list
        :param n2: position in cells list (if ==-9, then it's a storage, not a cell, so it's not taken into account)
        """
        if n2 != -9:
            self.board.cells[n1][n2].add_n_pieces(1)
        else:
            self.board.cells[n1].add_n_pieces(1)

    def next_player(self):
        """
        Determines who is the next player to make a move.
        """
        if not self.ended_move_on_piece:
            if self.active_player == self.board.players[0]:
                self.active_player = self.board.players[1]
            else:
                self.active_player = self.board.players[0]
            self.hint = self.active_player.name + "'s turn"
        else:
            self.ended_move_on_piece = False

    def is_players_cell(self, cell):
        """
        Determines whether the cell belongs to the active_player or not.

        :param cell: the cell whose appartenance needs to be checked.
        :return: True if active_player can click it, False if not.
        """
        if cell in self.active_player.allowed:
            return True
        else:
            return False
