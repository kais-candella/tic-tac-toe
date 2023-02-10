board = ["-" for x in range(9)]
currentPlayer = "X"
winner = None
gameRunning = True

def printBoard(board):
    print("|".join(board[0:3]))
    print("|".join(board[3:6]))
    print("|".join(board[6:9]))

def checkForWin(board):
    global winner

    # verif des rang

    for x in range(0,9,3):
        row = board[x:x+3]
        if row.count("X") == 3:
            winner = "X"
            return True
        elif row.count("O") == 3:
            winner = "O"
            return True

    # verification des colones


    for x in range(3):
        column = board[x::3]
        if column.count("X") == 3:
            winner = "X"
            return True
        elif column.count("O") == 3:
            winner = "O"
            return True


    # verif des diagonals


    diagonal1 = [board[0],board[4],board[8]]
    diagonal2 = [board[2],board[4],board[6]]
    if diagonal1.count("X") == 3 or diagonal2.count("X") == 3:
        winner = "X"
        return True
    elif diagonal1.count("O") == 3 or diagonal2.count("O") == 3:
        winner = "O"
        return True
    return False

def checkForTie(board):
    if "-" not in board:
        return True
    else:
        return False

while gameRunning:
    printBoard(board)
    print("It's player " + currentPlayer + "'s turn. Which box? (1-9)")
    move = int(input())-1
    if board[move] == "-":
        board[move] = currentPlayer
    else:
        print("That space is already filled. Pick again")
        continue
    if checkForWin(board):
        gameRunning = False
        printBoard(board)
        print("Player " + winner + " wins!")
    elif checkForTie(board):
        gameRunning = False
        print("Tie Game!")
    else:
        if currentPlayer == "X":
            currentPlayer = "O"
        else:
            currentPlayer = "X"


