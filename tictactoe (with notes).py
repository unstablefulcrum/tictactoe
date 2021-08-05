board=[["*","*","*"],["*","*","*"],["*","*","*"]]	#board is a 3x3 nested list

def toe(board,row,column,player):	#toe function is row and column selection, with an error check for a previously in space. It also saves the column and row selection to player item
    if board[row][column]!="*":
        raise ValueError
    board[row][column]=player

def printboard(board):	#printboard function prints the board list out in rows
    for boardrow in board:
        print(boardrow)

def winhor(board,player):	#winhor function checks to see if the player item is found in a row of the list. If it is, it returns a True value for later use. If not, a False value is output
    for boardrow in board:
        if boardrow==[player,player,player]:
            print("Player",player, "Wins!")
            return True
        else:
            return False

def winvert(board,player):	#winvert function checks to see if the player item is found in a column of the list. If it is, it returns a True value for later use. If not, a False value is output
    if board[0][0]==player and board[1][0]==player and board[2][0]==player:
        print("Player",player, "Wins!")
        return True
    elif board[0][1]==player and board[1][1]==player and board[2][1]==player:
        print("Player",player, "Wins!")
        return True
    elif board[0][2]==player and board[1][2]==player and board[2][2]==player:
        print("Player",player, "Wins!")
        return True
    else:
        return False

def windiag(board,player):	#windiag function check to see if the player item is found in a diagonal of the list. If it is, it returns a True value for later use. If not, a False value is output
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        print("Player",player, "Wins!")
        return True
    elif board[0][2]==player and board[1][1]==player and board[2][0]==player:
        print("Player",player, "Wins!")
        return True
    else:
        return False

def turn(board,player):	#turn function uses the board list and player item. While madevalidmove item is True, the player item is used in a printout, asking the current player to enter a row and a column for their marker
    madevalidmove=False
    while not madevalidmove:
        print("Player",player)
        row=input("Please type a Row:")
        column=input("Please type a Column:")
        try:	#try attempts to enter a marker by checking if the space is already filled by one using the toe function. If it is, it repeats the while loop, without changing the player, until a correct place is picked
            toe(board,int(row),int(column),player)
            madevalidmove=True
        except (ValueError, IndexError):
            print("Not a valid Space. Please choose another.")

def gameover(board):	#gameover function checks for a True win value to see if someone won. If no win, checks if the board is full. If yes, displays a Game Over, and ends the game. If not, keeps running.
    if winhor(board,player)==True or winvert(board,player)==True or windiag(board,player)==True:
        print("Game is Over. Good Game Player",player,"\b!")
        return True
    elif not any("*" in x for x in board):
        print("Game is Over. You both Lost!")
        print("---Better Luck Next Time---")
        return True
    else:
        return False

player="X"	#player item starts as X, and switches back and forth from X to O until the end of the game.

while not gameover(board):	#while not loop runs until the gameover variable is True. It prints the board, runs the turn function, checks for a win state after the turn is taken, then swaps the player items value
    printboard(board)
    turn(board,player)
    if winhor(board,player)==True:
        printboard(board)
        pass
    elif winvert(board,player)==True:
        printboard(board)
        pass
    elif windiag(board,player)==True:
        printboard(board)
        pass
    else:
        if player=="X":
            player="O"
        else:
            player="X"
