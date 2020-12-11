import re 
import math 

INPUT = '05/input1.txt'
ROW_COUNT = 128
COLUMN_COUNT = 8

FRONT = 'F'
BACK = 'B'
LEFT = 'L'
RIGHT = 'R'

seats = list()
with open(INPUT) as f:
    seats = f.read().splitlines()

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

def calculateSeatRange(seatRange, code):
    if code == BACK or code == RIGHT:
        newMin = math.ceil((seatRange[0] + seatRange[1])/2)
        newMax = seatRange[1]
    elif code == FRONT or code == LEFT:
        newMin = seatRange[0]
        newMax = math.floor((seatRange[0] + seatRange[1])/2)
    else:
        raise Exception('unknown seat code!', code)

    newSeatRange = (newMin, newMax)
    return newSeatRange

seatIds = list()

for seat in seats:
    rowRange = (0, ROW_COUNT - 1)
    columnRange = (0, COLUMN_COUNT - 1)

    for code in seat:
        if code == FRONT or code == BACK:
            rowRange = calculateSeatRange(rowRange, code)
        elif code == LEFT or code == RIGHT:
            columnRange = calculateSeatRange(columnRange, code)
        else:
            raise Exception('unkonwn seat code!', code)

    assert(rowRange[0] == rowRange[1], 'did not calculate final row!!!!')
    assert(columnRange[0] == columnRange[1], 'did not calculate final column!!!!')

    seatRow = rowRange[0]
    seatColumn = columnRange[0]

    seatId = seatRow * 8 + seatColumn
    seatIds.append(seatId)

print(max(seatIds))

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

seatIds.sort()
for i in range(len(seatIds) - 1):
    if seatIds[i] + 1 != seatIds[i+1]:
        print('Klopt niet! ', seatIds[i], ' -> ', seatIds[i+1])
