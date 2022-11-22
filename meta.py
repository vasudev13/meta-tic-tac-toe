from tictactoe import TicTacToe


class Meta:
    def __init__(self, check_game_state_fn):
        self.check_game_state_fn = check_game_state_fn
        self.cells = [
            [
                TicTacToe(check_game_state_fn) for _ in range(3)
            ] for _ in range(3)
        ]
        self.status = [
            [
                '.' for _ in range(3)
            ] for _ in range(3)
        ]

    def mark(self, game: list, coordinates: list, player: str):
        if self.status[game[0]][game[1]] == '.':
            status = self.cells[game[0]][game[1]].mark(coordinates, player)
            if status != '.':
                self.status[game[0]][game[1]] = status
                game_status = self.check_game_state_fn(self.status)
                return game_status
        else:
            print(self.status[game[0]][game[1]], ' already won that game')
            game_status = self.check_game_state_fn(self.status)
            return game_status

    def print_game(self):
        for i in range(3):
            for j in range(3):
                print('Game Cell: ', i,',',j)
                if self.status[i][j] == '.':
                    self.cells[i][j].print()
                else:
                    print(self.status[i][j], ' won the ', i,',',j, ' game')
                print('--' * 10)
