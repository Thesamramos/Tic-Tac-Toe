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