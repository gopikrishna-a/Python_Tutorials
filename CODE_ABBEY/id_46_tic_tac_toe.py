
def play_game(data):
    moves = 0
    for i, j in enumerate(data):
        moves += 1
        mark = "O"
        if i % 2 == 0:
            mark = "X"
        if j in range(1, 4):
            game_board[0][j - 1] = mark
        elif j in range(4, 7):
            game_board[1][j - 4] = mark
        elif j in range(7, 10):
            game_board[2][j - 7] = mark

        if game_board[0][0] == game_board[0][1] == game_board[0][2]:
            # print("Player {} Won!!!".format(game_board[0][0]))
            return moves
        elif game_board[1][0] == game_board[1][1] == game_board[1][2]:
            # print("Player {} Won!!!".format(game_board[1][0]))
            return moves
        elif game_board[2][0] == game_board[2][1] == game_board[2][2]:
            # print("Player {} Won!!!".format(game_board[2][0]))
            return moves

        elif game_board[0][0] == game_board[1][0] == game_board[2][0]:
            # print("Player {} Won!!!".format(game_board[1][0]))
            return moves
        elif game_board[0][1] == game_board[1][1] == game_board[2][1]:
            # print("Player {} Won!!!".format(game_board[2][0]))
            return moves
        elif game_board[0][2] == game_board[1][2] == game_board[2][2]:
            # print("Player {} Won!!!".format(game_board[2][0]))
            return moves

        elif game_board[0][0] == game_board[1][1] == game_board[2][2]:
            # print("Player {} Won!!!".format(game_board[2][0]))
            return moves
        elif game_board[0][2] == game_board[1][1] == game_board[2][0]:
            # print("Player {} Won!!!".format(game_board[2][0]))
            return moves
    return 0



if __name__ == "__main__":
    n = int(input())
    result = []
    for game in range(n):
        game_board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        data = list(map(int, input().split()))
        result.append(play_game(data))
    print(" ".join(map(str, result)))
