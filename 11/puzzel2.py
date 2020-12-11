import re

INPUT = '11/input1.txt'

print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

# # test based on example
# inputFile = (
#     'L.LL.LL.LL', 
#     'LLLLLLL.LL', 
#     'L.L.L..L..', 
#     'LLLL.LL.LL', 
#     'L.LL.LL.LL', 
#     'L.LLLLL.LL', 
#     '..L.L.....', 
#     'LLLLLLLLLL', 
#     'L.LLLLLL.L', 
#     'L.LLLLL.LL'
# )

# create 2D grid
waitingArea = list()
for row in inputFile:
    row = row.strip()
    waitingArea.append([ seat for seat in row ])
xSize = len(waitingArea)
ySize = len(waitingArea[0])

# init constants
EMPTY = 'L'
OCCUPIED = '#'
FLOOR = '.' 

def getFirstSeatInDirection(xPos, yPos, xDiff, yDiff, seatArea):
    xCheck = xPos + xDiff
    yCheck = yPos + yDiff

    while(
        # validate whether these are valid positions
        xCheck >=0 and xCheck < xSize and
        yCheck >=0 and yCheck < ySize and
        # continue checking if we come across a floor
        seatArea[xCheck][yCheck] == FLOOR
    ):
        xCheck += xDiff
        yCheck += yDiff

    if(
        # validate whether these are valid positions
        xCheck >=0 and xCheck < xSize and
        yCheck >=0 and yCheck < ySize
    ):
        return seatArea[xCheck][yCheck]
    else:
        return False

def changeSeat(xPos, yPos, seatArea):
    # all adhecent seats are to be checked
    directionToCheck = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    occupiedCount = 0

    # count amount of occupied seats next to this one
    for (xDiff, yDiff) in directionToCheck:
        firstSeatInDirection = getFirstSeatInDirection(xPos, yPos, xDiff, yDiff, seatArea)
        occupiedCount += firstSeatInDirection == OCCUPIED
    
    # calculate the new seat status
    currentSeatStatus = seatArea[xPos][yPos]
    if(
        currentSeatStatus == EMPTY and
        occupiedCount == 0
    ):
        newSeatStatus = OCCUPIED
    elif(
        currentSeatStatus == OCCUPIED and
        occupiedCount >= 5
    ):
        newSeatStatus = EMPTY
    else:
        newSeatStatus = currentSeatStatus
    
    return newSeatStatus

def printSeatArea(seatArea):
    for row in seatArea:
        for seat in row:
            print(seat, end='')
        print()
    print()

def iterateSeatArea(seatArea):
    # create deep copy of seatArea
    newWaitingArea = [[seat for seat in row] for row in waitingArea]

    # iterate overall seats
    occupiedSeatCount = 0
    for x in range(xSize):
        for y in range(ySize):
            newSeatStatus = changeSeat(x, y, waitingArea)
            occupiedSeatCount += newSeatStatus == OCCUPIED
            newWaitingArea[x][y] = newSeatStatus

    return (newWaitingArea, occupiedSeatCount)
    
printSeatArea(waitingArea)

currentOccupiedSeatCount = -1
newOccupiedSeatCount = 0
while currentOccupiedSeatCount != newOccupiedSeatCount:
    currentOccupiedSeatCount = newOccupiedSeatCount
    (waitingArea, newOccupiedSeatCount) = iterateSeatArea(waitingArea)
    printSeatArea(waitingArea)

print(newOccupiedSeatCount)