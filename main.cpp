def draw_board(board):
    print("-------------")
    for i in range(len(board)):
        print("| ", end="")
        for j in range(len(board[i])):
            print(board[i][j], "| ", end="")
        print("\n-------------")

rows = 3
cols = 3
board = [[' ' for _ in range(cols)] for _ in range(rows)]
draw_board(board)
