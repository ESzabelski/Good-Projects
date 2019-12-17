
import pygame, sys, random
from pygame.locals import *

WINDOW_HEIGHT=480
WINDOW_WIDTH=640
CELL_SIZE=8
FPS=10

assert WINDOW_WIDTH % CELL_SIZE==0 #must be divisible by cell side
assert WINDOW_HEIGHT % CELL_SIZE==0
CELL_WIDTH=WINDOW_WIDTH//CELL_SIZE
CELL_HEIGHT=WINDOW_HEIGHT//CELL_SIZE

BLACK= (0,0,0)
WHITE=(255,255,255)
DARKGRAY=(40,40,40)
GREEN=(0,255,0)
RED=(255,0,0)

def drawGrid():
    for x in range(0,WINDOW_WIDTH,CELL_SIZE): #VERTICAL LINES
        pygame.draw.line(DISPLAYSURF,DARKGRAY, (x,0),(x,WINDOW_HEIGHT))
    for y in range (0,WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(DISPLAYSURF,DARKGRAY,(0,y),(WINDOW_WIDTH,y))


def blankGrid():
    gridDict={}
    for y in range(CELL_HEIGHT):
        for x in range(CELL_WIDTH):
            gridDict[x,y]=0 #0 represents a dead cell
    return gridDict


def startingGridRandom(lifeDict): #this takes a blank complete dictionary
    pred=0                              # and randomally assigns 'life' (1) to some
    
    for i in lifeDict:
        if pred<6:
            r=random.randint(0,300)
            if r==300:
                lifeDict[i]=2
                pred+=1
            else:
                lifeDict[i]=random.randint(0,1)
        else:
            lifeDict[i]=random.randint(0,1)
    return lifeDict

def colorGrid(item,lifeDict): #draws rectangles based on 'live' or 'dead'
    x=item[0]
    y=item[1]
    y=y*CELL_SIZE #this is to keep consistent with the cell size
    x=x*CELL_SIZE

    if lifeDict[item]==0:
        pygame.draw.rect(DISPLAYSURF,WHITE, (x,y,CELL_SIZE,CELL_SIZE))
    if lifeDict[item]==1:
        pygame.draw.rect(DISPLAYSURF,GREEN, (x,y,CELL_SIZE,CELL_SIZE))
    if lifeDict[item]==2:
        pygame.draw.rect(DISPLAYSURF,RED, (x,y,CELL_SIZE,CELL_SIZE))         
    return None


def getNeighbors (item,lifeDict):
    neighbors=0
    preds=0
    for x in range(-1,2): #checks all 8 directions around a cell
        for y in range(-1,2):
            checkCell=(item[0]+x, item[1]+y)
            if checkCell[0]<CELL_WIDTH and checkCell[0]>=0: #checks to exclude off board cells
                if checkCell[1]<CELL_HEIGHT and checkCell[1]>0: #checks legal height

                    if lifeDict[checkCell]==1: #current cell has life
                        if x==0 and y==0: #actual cell, ignore
                            neighbors+=0
                        else:
                            neighbors+=1
                            
                    if lifeDict[checkCell]==2: #current cell is a pred
                        if x==0 and y==0: #actual cell, ignore
                            preds+=0
                        else:
                            preds+=1                            
    return neighbors, preds


#do some pred things to the new tick
def tick(lifeDict):
    newTick={}
    for i in lifeDict:
        number_of_neighbors, number_of_preds=getNeighbors(i,lifeDict)

        #1,4,4 is a cool maze pattern
        if lifeDict[i]==1: #these apply to live cells
            if number_of_neighbors <2: #2
                newTick[i]=0 #dies by underpopulation
            elif number_of_neighbors > 3: #3
                newTick[i]=0
            elif number_of_preds>=2: ##pred check #2
                newTick[i]=0
            else:
                newTick[i]=1 #stable at 2-3 neighbors


        elif lifeDict[i]==0: #a current dead cell
            if number_of_neighbors==3 and number_of_preds<2: #a new life is born here
                newTick[i]=1
            elif number_of_neighbors>0 and number_of_preds==1: #pred born
                newTick[i]=2
            else:
                newTick[i]=0 #no change

        elif lifeDict[i]==2:#### a pred
            if number_of_neighbors>0:
                newTick[i]=2 #perhaps add pred overpopulation
            else:
                newTick[i]=0
            

            
    return newTick
            





def main():
    pygame.init()
    global DISPLAYSURF
    FPSCLOCK=pygame.time.Clock()
    
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption("Game of Life")
    DISPLAYSURF.fill(WHITE)
    blankDict=blankGrid() #creates the dictionary of all empty/dead cells
    lifeDict=startingGridRandom(blankDict) #randomly assigns some cells as alive 

    for i in lifeDict:
        colorGrid(i,lifeDict)
    
    drawGrid()
    pygame.display.update()
    blankGrid()

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

        lifeDict=tick(lifeDict) #runs a single tick
        for i in lifeDict:
            colorGrid(i,lifeDict) #colors the new cells
        drawGrid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

        
        

if __name__=='__main__':
    main()




#add a predator
    #while len pred <4
        #try putting it into a spot
