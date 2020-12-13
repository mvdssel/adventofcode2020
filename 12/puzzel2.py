import re

INPUT = '12/input1.txt'

print("------------------------------------------")
print("          PUZZEL 2")
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

    currentEast = 0
    currentNorth = 0

    wayPointEast = 10
    wayPointNorth = 1

    def __init__(self):
        print('new boat created')
    
    def print(self):
        print('{0:2d} x {1:2d} | {2:2d} x {3:2d}'.format(self.currentEast, self.currentNorth, self.wayPointEast, self.wayPointNorth))

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
        
        self.print()

    def moveEast(self, distance):
        print('moving {} to the east'.format(distance))
        self.wayPointEast += distance

    def moveWest(self, distance):
        print('moving {} to the west'.format(distance))
        self.wayPointEast -= distance

    def moveNorth(self, distance):
        print('moving {} to the north'.format(distance))
        self.wayPointNorth += distance

    def moveSouth(self, distance):
        print('moving {} to the south'.format(distance))
        self.wayPointNorth -= distance

    def moveLeft(self, degrees):
        print('rotating {} to the left'.format(degrees))

        self.moveRight(360 - degrees)

    def moveRight(self, degrees):
        print('rotating {} to the right'.format(degrees))

        degrees = degrees % 360

        for i in range(int(degrees / 90)):
            self.rotateQuater()
    
    def rotateQuater(self):
        if self.wayPointEast >= 0 and self.wayPointNorth >= 0:
            newWayPointEast = self.wayPointNorth
            newWayPointNorth = -self.wayPointEast
        elif self.wayPointEast >= 0 and self.wayPointNorth <= 0:
            newWayPointEast = self.wayPointNorth
            newWayPointNorth = -self.wayPointEast
        elif self.wayPointEast <= 0 and self.wayPointNorth <= 0:
            newWayPointEast = self.wayPointNorth
            newWayPointNorth = -self.wayPointEast
        elif self.wayPointEast <= 0 and self.wayPointNorth >= 0:
            newWayPointEast = self.wayPointNorth
            newWayPointNorth = -self.wayPointEast
        
        self.wayPointEast = newWayPointEast
        self.wayPointNorth = newWayPointNorth
    
    def moveForward(self, distance):
        print('moving {} to the forward'.format(distance))
        self.currentNorth += self.wayPointNorth * distance
        self.currentEast += self.wayPointEast * distance


ferry = Boat()

for instruction in instructions:
    ferry.move(instruction[0], instruction[1])

ferry.move('L', 90)
ferry.move('L', 90)
ferry.move('L', 90)
ferry.move('L', 90)
ferry.move('L', 180)
ferry.move('L', 270)

print('north: {} | east: {}'.format(ferry.currentNorth, ferry.currentEast))
print('{} + {} = {}'.format(ferry.currentNorth, ferry.currentEast, ferry.getManhattanDistance()))
