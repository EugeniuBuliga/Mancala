class Player:
    def __init__(self, board, name, orientation):
        self.board = board
        self.name = name
        self.orientation = orientation

        self.storage_num = -1
        self.storage, self.allowed = self.get_allowed_cells()

    def __str__(self):
        return "<Player-" + self.orientation + "> " + self.name

    def __repr__(self):
        return self.__str__()

    def get_storage(self) -> int:
        """
        Get the storage number of the player (0 = right, 1 = left)

        :return: 0 or 1
        """
        return self.storage_num

    def get_allowed_cells(self) -> (int, list):
        """
        Sets the list of cells upon which the player can click, plus the respective storage.

        :return: player's piece storage, cells allowed to click
        """
        if self.orientation == "up":
            allowed = self.board.cells[2]
            storage = self.board.cells[0]
            self.storage_num = 0
        else:
            allowed = self.board.cells[3]
            storage = self.board.cells[1]
            self.storage_num = 1
        return storage, allowed
