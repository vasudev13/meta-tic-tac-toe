class TicTacToe:

    def __init__(self, check_state_fn):
        """
        Implementation of individual game in the meta game
        :param check_state_fn: function that checks whether the game has concluded given the state of cells.
        """
        self.cells = [
            [
                '.' for _ in range(3)
            ] for _ in range(3)
        ]
        self.is_game_over = False
        self.check_state_fn = check_state_fn

    def mark(self, coordinates: list, player: str):
        x, y = coordinates
        if self.cells[x][y] == '.':
            self.cells[x][y] = player
            status = self.check_state_fn(self.cells)
            return status
        else:
            print('[ERROR]: Cannot override already marked cell !!')
            return False

    def print(self):
        for i in range(3):
            for j in range(3):
                print(self.cells[i][j], end='|')
            print('\n-+-+-')
