INPUT = '03/input1.txt'

input = list()
with open(INPUT) as f:
    input = f.read().splitlines()

print()
print("------------------------------------------")
print("          puzzel 1")
print("------------------------------------------")
print()

TREE = '#'

def traverseSlope(incX, inxY):
    posX = 0
    posY = 0
    treeCount = 0

    while(posY < len(input)):
        altPosX = posX % len(input[0])
        altPosY = posY % len(input)
        if(input[altPosY][altPosX] == TREE):
            treeCount += 1

        posX += incX
        posY += incY
    
    return treeCount

result = 1

slopes = (
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
)
for slope in slopes:
    incX = slope[0]
    incY = slope[1]
    treeCount = traverseSlope(incX, incY)
    print('x: {}, y: {} => {}'.format(incX, incY, treeCount))

    result *= treeCount

print('result: ', result)

print()
print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")
print()
