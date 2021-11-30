import pygame


class Logic:
    def __init__(self, board):
        self.board = board
        self.active_player = board.players[0]
        self.move_made = False
        self.ended_move_on_piece = False
        self.hint1 = self.active_player.name + " start the game"
        self.hint2 = ""
        self.last_cell = board.cells[0]
        self.ended = False

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
                        if not self.capture():
                            self.hint2 = ""
                self.check_win_state(i)

    def check_win_state(self, i):
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

    def get_winner(self):
        if len(self.board.players[0].storage.inventory) > len(self.board.players[1].storage.inventory):
            return self.board.players[0]
        elif len(self.board.players[0].storage.inventory) < len(self.board.players[1].storage.inventory):
            return self.board.players[1]
        else:
            return "both"

    def capture(self):
        if len(self.last_cell.inventory) == 1 and not self.last_cell.is_storage:
            if self.transfer_pieces(self.opposite_cell(self.last_cell), self.active_player.storage):
                self.hint2 = self.active_player.name + " captured opponent's pieces"
                return True
        return False

    def opposite_cell(self, cell):
        if cell.cell_type == "upper":
            opposite = self.board.cells[3][int(cell.order)]
        else:
            opposite = self.board.cells[2][int(cell.order)]
        return opposite

    @staticmethod
    def transfer_pieces(cell1, cell2):
        if cell1.inventory:
            while cell1.inventory:
                cell2.add_n_pieces(1)
                cell1.remove_piece()
            return True
        else:
            return False

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
            self.move_made = True
        if actual_i == 0 or actual_i == 1:
            self.ended_move_on_piece = True
            self.last_cell = self.board.cells[actual_i]
        else:
            self.last_cell = self.board.cells[actual_i][actual_j]

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
            self.hint1 = self.active_player.name + "'s turn"
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
