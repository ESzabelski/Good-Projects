
import random
import sys
WIDTH = 8
HEIGHT =8
def drawBoard(board):

    print("  12345678")
    print(" +--------+")
    for y in range(HEIGHT):
        print("%s|" %(y+1),end="")
        for x in range( WIDTH):
            print(board[x][y],end="") #this all prints 3 things at once, left side, iters the posistions, then the right side
        print("%s|" %(y+1))
    print(" +--------+")
    print("  12345678")

def getNewBoard():
    #makes a brand new board, adds 8 slots, 8 times
    board=[]
    for i in range(WIDTH):
        #board.append( [" "]*8)
        board.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    #returns false if move is invalid
    #if valid returns a list of spaces that would switch if moved here
    if board[xstart][ystart] != " " or not isOnBoard(xstart, ystart): #checks the spot is in 8x8 grid and also blank
        return False

    if tile == "X":
        otherTile="O"
    else:
        otherTile="X"

    tilesToFlip=[]
    for xdirection,ydirection in [[0, 1], [1, 1], [1, 0], [1, -1],[0, -1], [-1, -1], [-1, 0], [-1, 1]]: #checks all 8 directions it could be 
        x,y =xstart,ystart
        x+=xdirection 
        y+= ydirection #so it will iter all 8 options, then below see if this is a legal move and potentially flips tiles
        while isOnBoard(x,y) and board[x][y]==otherTile:
            #keep moving
            x+=xdirection
            y+=ydirection
            if isOnBoard(x,y) and board[x][y]==tile:
                #There are peices to flip over, so this checks that it is a 'flippable
                #move, so then go backwards to add to the flip list
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x==xstart and y==ystart:
                        break
                    tilesToFlip.append([x,y])
                
    if len(tilesToFlip)==0: #no tiles would flip, so invalid move
        return False
    return tilesToFlip

def isOnBoard(x,y):
    #checks to make sure move is on the board
    return x>=0 and x<=WIDTH-1 and y>=0 and y<=HEIGHT-1

def getBoardWithValidMoves(board,tile):
    #shows a board with every legal move for player
    boardCopy=getBoardCopy(board)
    for x,y in getValidMoves(boardCopy,tile):
        boardCopy[x][y]="."
    return boardCopy

def getValidMoves(board,tile):
    #returns a list of all legal player moves
    validMoves=[]
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board,tile,x,y) !=False:
                validMoves.append([x,y])
    return validMoves

def getScoreOfBoard(board):
    #counts score through returning a dictionary using keys X and O
    xscore=0
    oscore=0
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y]=="X":
                xscore+=1
            if board[x][y]=="O":
                oscore+=1
    return {"X":xscore, "O":oscore}


def enterPlayerTile():
    #pick what tile to be

    tile=""
    while not (tile=="X" or tile=="O"):
        print("Do you want to be X or O?")
        tile=input().upper()

    if tile=="X":
        return ["X","O"]
    else:
        return["O","X"]


def whoGoesFirst():
    #randomly decides
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'

def makeMove(board,tile,xstart,ystart):
    #places tile at x,ystart and flips any enemy tiles
    #False if invalid move
    tilesToFlip=isValidMove(board,tile,xstart,ystart)

    if tilesToFlip==False:
        return False

    board[xstart][ystart]=tile
    for x,y in tilesToFlip:
        board[x][y]=tile
    return True

def getBoardCopy(board):
    #makes a list copy of the board
    boardCopy=getNewBoard()
    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y]=board[x][y]

    return boardCopy


def isOnCorner(x,y):
    #returns true if posistion is a corner
    return (x == 0 or x == WIDTH - 1) and (y == 0 or y == HEIGHT - 1)

def getPlayerMove(board,playerTile):
    #lets player enter their move, also allows 'hints' or 'quit'
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print("Enter your move, 'quit' to end or 'hints' for hint mode")
        move=input().lower()
        if move=="quit" or move=="hints":
            return move

        if len(move)==2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x=int(move[0])-1
            y=int(move[1])-1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print("Not a valid move, enter a column (1-8) and row (1-8)")
            print("Eg. 81 is top right corner")
    return [x,y]



def getComputerMove(board,computerTile):
    #takes the tile, and board, gives a list of all moves, then
    #decides on specific move
    possibleMoves=getValidMoves(board,computerTile)
    random.shuffle(possibleMoves)

    #always take corner
    for x,y in possibleMoves:
        if isOnCorner(x,y):
            return [x,y]

    #finds highest scoring move
    bestScore=-1
    for x,y in possibleMoves:
        boardCopy=getBoardCopy(board)
        makeMove(boardCopy,computerTile,x,y)
        score=getScoreOfBoard(boardCopy)[computerTile]
        if score>bestScore:
            bestMove=[x,y]
            bestScore=score
    return bestMove

def printScore(board,playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile],scores[computerTile]))

def playGame (playerTile, computerTile):
    showHints=False
    turn=whoGoesFirst()
    print("The " + turn + " will go first")

    board=getNewBoard()
    board[3][3]= "X"
    board[3][4]= "O"
    board[4][3]= "O"
    board[4][4]= "X"

    while True:
        playerValidMoves=getValidMoves(board,playerTile)
        computerValidMoves=getValidMoves(board,computerTile)

        if playerValidMoves==[] and computerValidMoves==[]:
            return board #no moves left

        elif turn =="player" :
            if playerValidMoves !=[]:
                if showHints:
                    validMovesBoard=getBoardWithValidMoves(board, playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board,playerTile,computerTile)

                move=getPlayerMove(board, playerTile)
                if move=="quit":
                    print("Thanks for playing!")
                    sys.exit()
                elif move=="hints":
                    showHints= not showHints
                    continue
                else:
                    makeMove(board,playerTile,move[0],move[1])
            turn="computer"

        elif turn =="computer":
            if computerValidMoves!=[]:
                drawBoard(board)
                printScore(board,playerTile,computerTile)

                input("Press enter to see computer's move")
                move=getComputerMove(board,computerTile)
                makeMove(board, computerTile, move[0],move[1])
            turn="player"

print("Welcome to Reversi!")

playerTile, computerTile=enterPlayerTile()

while True:
    finalBoard=playGame(playerTile, computerTile)

    #Displays final score
    drawBoard(finalBoard)
    scores=getScoreOfBoard(finalBoard)
    print('X scored %s points. O scored %s points.' % (scores['X'],scores['O']))
    if scores[playerTile]>scores[computerTile]:
        print("You beat the computer!")
    elif scores[playerTile]<scores[computerTile]:
        print("You lost.")
    else:
        print("You tied!")

    print("Want to play again?")
    if not input().lower().startswith("y"):
        break











        







































    
























        































        

