import re

INPUT = '12/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')
# # example
# inputFile = [
#     'F10',
#     'N3',
#     'F7',
#     'R90',
#     'F11'
# ]

NORTH = 'N'
EAST = 'E'
SOUTH = 'S'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'

instructions = list()
for line in inputFile:
    (action, value) = (line[0], int(line[1:]))
    instructions.append((action, value))


class Boat:
    DIRECTIONS = [NORTH, EAST, SOUTH, WEST]

    currentDirectionIndex = 1
    currentEast = 0
    currentNorth = 0

    def __init__(self):
        print('new boat created')

    def getCurrentDirection(self):
        return self.DIRECTIONS[self.currentDirectionIndex]

    def getManhattanDistance(self):
        return abs(self.currentEast) + abs(self.currentNorth)

    def move(self, direction, distance):
        if direction == EAST:
            self.moveEast(distance)
        elif direction == WEST:
            self.moveWest(distance)
        elif direction == NORTH:
            self.moveNorth(distance)
        elif direction == SOUTH:
            self.moveSouth(distance)
        elif direction == LEFT:
            self.moveLeft(distance)
        elif direction == RIGHT:
            self.moveRight(distance)
        elif direction == FORWARD:
            self.moveForward(distance)

    def moveEast(self, distance):
        print('moving {} to the east'.format(distance))
        self.currentEast += distance

    def moveWest(self, distance):
        print('moving {} to the west'.format(distance))
        self.currentEast -= distance

    def moveNorth(self, distance):
        print('moving {} to the north'.format(distance))
        self.currentNorth += distance

    def moveSouth(self, distance):
        print('moving {} to the south'.format(distance))
        self.currentNorth -= distance

    def moveLeft(self, distance):
        print('moving {} to the left'.format(distance))
        self.currentDirectionIndex = int(
            self.currentDirectionIndex - distance / 90) % len(self.DIRECTIONS)

    def moveRight(self, distance):
        print('moving {} to the right'.format(distance))
        self.currentDirectionIndex = int(
            self.currentDirectionIndex + distance / 90) % len(self.DIRECTIONS)

    def moveForward(self, distance):
        print('moving {} to the forward'.format(distance))
        curDir = self.getCurrentDirection()
        if curDir == NORTH:
            self.currentNorth += distance
        elif curDir == EAST:
            self.currentEast += distance
        elif curDir == SOUTH:
            self.currentNorth -= distance
        elif curDir == WEST:
            self.currentEast -= distance
        else:
            raise Exception('Something went wrong :-/')


ferry = Boat()

for instruction in instructions:
    ferry.move(instruction[0], instruction[1])

print('north: {} | east: {}'.format(ferry.currentNorth, ferry.currentEast))
print('{} + {} = {}'.format(ferry.currentNorth, ferry.currentEast, ferry.getManhattanDistance()))
