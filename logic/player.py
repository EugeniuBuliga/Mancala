class Player:
    def __init__(self, board, name, orientation):
        self.board = board
        self.name = name
        self.orientation = orientation

        self.storage, self.allowed = self.get_allowed_cells()

    def __str__(self):
        return "<Player-" + self.orientation + "> " + self.name

    def __repr__(self):
        return self.__str__()

    def get_allowed_cells(self):
        if self.orientation == "up":
            allowed = self.board.cells[2]
            storage = self.board.cells[0]
        else:
            allowed = self.board.cells[3]
            storage = self.board.cells[1]
        # print(self.name,"allowed to move on", allowed, "stores in", storage)
        return storage, allowed
