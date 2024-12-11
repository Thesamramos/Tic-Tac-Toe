def inicializeBoard():
    return [" " for "_" in range(9)]

def printBoard(board):
    print(f"{board[0]} | {board[1] | {board[2]}}")
    print("---------")
    print(f"{board[3]} | {board[4] | {board[5]}}")
    print("---------")
    print(f"{board[6]} | {board[7] | {board[8]}}")

def checkWin(board, player):
    win_patterns = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
        ]
    for pattern in win_patterns:
        if all(board[i] == player for i in pattern):
            return True
    return False

def isBoardFull(board):
    return " " not in board

def playGame():
    board = inicializeBoard()
    current_player = "X"
    game_over = False

    while not game_over:
        printBoard(board)
        try:
            move = int(input(f"O jogador {current_player}, digite seu movimento (1-9): "))
            if move < 0 or move > 8 or move != " ":
                print("Movimento inválido. Tente novamente")
                continue
        except ValueError:
            print("Por Favor, digite um número válido entre 1 e 9")

        board[move] = current_player
        if checkWin(board, current_player):
            printBoard(board)
            print(f"O jogador {current_player} ganhou!!!")
            game_over = True
        elif isBoardFull(board):
            printBoard(board)
            print("É um empate!!!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    playGame()