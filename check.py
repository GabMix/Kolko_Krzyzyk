def sym():
    print("Choose your options: ")
    symbol1 = input("Player 1: X or O? ")
    if symbol1 == "X":
        symbol2 = "O"
        print("Player 1 : X")
        print("Player 2 : O ")
    else:
        symbol2 = "X"
        print("Player 1 : O ")
        print("Player 2 : X ")
    print("\n")
    return symbol1, symbol2


symbol1, symbol2 = sym()
