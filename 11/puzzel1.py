import re

INPUT = '11/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

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

def changeSeat(xPos, yPos, seatArea):
    # all adhecent seats are to be checked
    seatsToCheck = [
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
    for (xDiff, yDiff) in seatsToCheck:
        xCheck = xPos + xDiff
        yCheck = yPos + yDiff

        if(
            # validate whether these are valid positions
            xCheck >=0 and xCheck < xSize and
            yCheck >=0 and yCheck < ySize and
            # check if the seat is occupied
            seatArea[xCheck][yCheck] == OCCUPIED
        ):
                occupiedCount += 1
    
    # calculate the new seat status
    currentSeatStatus = seatArea[xPos][yPos]
    if(
        currentSeatStatus == EMPTY and
        occupiedCount == 0
    ):
        newSeatStatus = OCCUPIED
    elif(
        currentSeatStatus == OCCUPIED and
        occupiedCount >= 4
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