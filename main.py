from meta import Meta

PLAYER_X_TURN = True


def check_game_status(cells):
    for i in range(3):
        if cells[i][0] == cells[i][1] == cells[i][2]:
            return cells[i][0]
    for i in range(3):
        if cells[0][i] == cells[1][i] == cells[2][i]:
            return cells[0][i]
    if cells[0][0] == cells[1][1] == cells[2][2]:
        return cells[0][0]
    if cells[0][2] == cells[1][1] == cells[2][1]:
        return cells[1][1]
    return '.'


if __name__ == '__main__':
    game = Meta(check_game_status)
    print('Meta Tic Tac Toe!!')
    game.print_game()
    while True:
        print('Player X') if PLAYER_X_TURN else print('Player O')
        game_coordinates = input('Enter Game to mark cell\n')
        game_coordinates = [int(x) for x in game_coordinates.strip().split(' ')]
        print(game_coordinates)
        coordinates = input('Enter cell to mark in chosen game\n')
        coordinates = [int(x) for x in coordinates.strip().split(' ')]
        print(coordinates)
        if PLAYER_X_TURN:
            status = game.mark(game_coordinates, coordinates, 'X')
            if status != '.':
                print(status, ' won the game')
                break
        else:
            status = game.mark(game_coordinates, coordinates, 'O')
            if status != '.':
                print(status, ' won the game')
                break
        PLAYER_X_TURN = not PLAYER_X_TURN
        game.print_game()
