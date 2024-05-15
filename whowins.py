COL = 3
ROW = 3

symbol1 = 'X'
symbol2 = 'O'
def who_win(board, symbol1, symbol2):
    playerXWinner = False
    playerOWinner = False
    #symbol 1 - X, symbol2 - O

    #poglad sytuacji rozmieszczenia
    #[board[0][0], board[1][0], board[2][0]],
    #[board[0][1], board[1][1], board[2][1]],
    #[board[0][2], board[1][2], board[2][2]],
    # sprawdzam kolumny
    for i in range(0, COL):
        if board[0][i] == board[1][i] == board[2][i] == symbol1:
            playerXWinner = True
            playerOWinner = False
            # print("Player X wins! ")
            return playerXWinner, playerOWinner
        elif board[0][i] == board[1][i] == board[2][i] == symbol2:
            playerOWinner = True
            playerXWinner = False
            # print("Player O wins! ")
            return playerXWinner, playerOWinner
    #sprawdzam wiersze
    for i in range(0, ROW):
        if board[i][0] == board[i][1] == board[i][2] == symbol1:
            playerXWinner = True
            playerOWinner = False
            # print("Player X wins! ")
            return playerXWinner, playerOWinner
        elif board[i][0] == board[i][1] == board[i][2] == symbol2:
            playerOWinner = True
            playerXWinner = False
            # print("Player O wins!")
            return playerXWinner, playerOWinner
    #diagonal
    if board[0][0] == board[1][1] == board[2][2] == symbol1 or board[0][2] == board[1][1] == board[2][0] == symbol1:
        playerXWinner = True
        playerOWinner = False
        # print("Player X wins! ")
        return playerXWinner, playerOWinner
    elif board[0][0] == board[1][1] == board[2][2] == symbol2 or board[0][2] == board[1][1] == board[2][0] == symbol2:
        playerOWinner = True
        playerXWinner = False
        # print("Player O wins! ")
        return playerXWinner, playerOWinner

# board = [
#     ['X', 'O', 'X'],
#     ['X', 'X', 'O'],
#     ['O', 'X', 'O']
# ]
# who_win(board,symbol1, symbol2)

