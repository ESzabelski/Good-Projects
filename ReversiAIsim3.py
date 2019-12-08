##This is a model and simulation of the reversi/othello game.  This includes
##multiple ais, as well as other insights such as how often corners
##correlate to winning.
##go into the playgame() section to pick which ai to pit against the others



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


##def whoGoesFirst():
##    #randomly decides
##    if random.randint(0,1)==0:
##        return 'computer'
##    else:
##        return 'player'


def whoGoesFirst():
    #randomly decides
##    if random.randint(0,1)==0:
##        return 'computer'
##    else:
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



def getCornerBestMove(board,computerTile):
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

def getWorstMove(board, tile):
    # Return the move that flips the least number of tiles.
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves) # Randomize the order of the moves.

    # Go through all the possible moves and remember the best scoring move.
    worstScore = 64
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, tile, x, y)
        score = getScoreOfBoard(boardCopy)[tile]
        if score < worstScore:
            worstMove = [x, y]
            worstScore = score

    return worstMove

def getRandomMove(board, tile):
    possibleMoves = getValidMoves(board, tile)
    return random.choice(possibleMoves)

def isOnSide(x, y):
    return x == 0 or x == WIDTH - 1 or y == 0 or y == HEIGHT - 1

def getCornerSideBestMove(board, tile):
    # Return a corner move, or a side move, or the best move.
    possibleMoves = getValidMoves(board, tile)
    random.shuffle(possibleMoves) # Randomize the order of the moves.

    # Always go for a corner if available.
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # If there is no corner, return a side move.
    for x, y in possibleMoves:
        if isOnSide(x, y):
            return [x, y]

    return getCornerBestMove(board, tile) # Do what the normal AI would do.


def printScore(board,playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: %s points. Computer: %s points.' % (scores[playerTile],scores[computerTile]))

def playGame (playerTile, computerTile):
    showHints=False
    turn=whoGoesFirst()
    #print("The " + turn + " will go first")

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


#change this section for the better ai
        elif turn =="player" :
            if playerValidMoves !=[]:
                #move=getComputerMove(board, playerTile)  ##this goes back to reg ai
                move = getCornerBestMove(board, playerTile)
                #move = getWorstMove(board, playerTile)
                #move=getRandomMove(board,playerTile)
                makeMove(board,playerTile,move[0],move[1])
            turn="computer"

#change this section for the worse co
        elif turn =="computer":
            if computerValidMoves!=[]:
                move = getCornerBestMove(board, computerTile) ##reg ai
                #move = getWorstMove(board, computerTile)
                #move = getRandomMove(board, computerTile)
                #move = getCornerSideBestMove(board, computerTile)
                makeMove(board, computerTile, move[0],move[1])
            turn="player"
NUM_GAMES=100
xWins=oWins=ties=0
print("Welcome to Reversi!")

playerTile, computerTile=['X','O'] #enterPlayerTile()


corner_average=[]
for i in range(NUM_GAMES): #while True:
    finalBoard = playGame(playerTile, computerTile)
    corner_count=0
    
    # Display the final score.
    #drawBoard(finalBoard)
    #print(finalBoard[0][0],finalBoard[0][7],finalBoard[7][0],finalBoard[7][7])
    scores = getScoreOfBoard(finalBoard)
    #print('#%s: X scored %s points. O scored %s points.' % (i + 1, scores['X'], scores['O']))
    if scores[playerTile] > scores[computerTile]:
        xWins += 1 #print('You beat the computer by %s points! Congratulations!' % (scores[playerTile] - scores[computerTile]))
        for i in (finalBoard[0][0],finalBoard[0][7],finalBoard[7][0],finalBoard[7][7]):
            if i =="X":
                corner_count+=1
        if corner_count==0:
            print("                              X WON WITHOUT A CORNER")
        print("X won with this many corners: " +str(corner_count))
        corner_average.append(corner_count)
    elif scores[playerTile] < scores[computerTile]:
        oWins += 1 #print('You lost. The computer beat you by %s points.' % (scores[computerTile] - scores[playerTile]))
    else:
        ties += 1 #print('The game was a tie!')

    #print('Do you want to play again? (yes or no)')
    #if not input().lower().startswith('y'):
    #    break


average=sum(corner_average)/len(corner_average)
print("When X won, the corner average was " +str(average))

print('X wins: %s (%s%%)' % (xWins, round(xWins / NUM_GAMES * 100, 1)))
print('O wins: %s (%s%%)' % (oWins, round(oWins / NUM_GAMES * 100, 1)))
print('Ties:   %s (%s%%)' % (ties, round(ties / NUM_GAMES * 100, 1)))



        







































    
























        































        

