import re

INPUT = '09/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')
numbers = [ int(line) for line in inputFile ]

def isValidNumber(number, previousNumbers):
    validated = False

    for i in range(len(previousNumbers)):
        for j in range(i+1, len(previousNumbers)):
            sum = previousNumbers[i] + previousNumbers[j]
            if number == sum:
                # Found a match!
                # print('\t', previousNumbers[i], ' + ', previousNumbers[j], ' = ', sum)
                validated = True
                break
            # elif sum > number:
            #     # Stop looking if the sum stats to get bigger than our number
            #     break
        
        if validated:
            # Stop looking if a match was found
            break
    
    return validated

for i in range(25, len(numbers)):
    number = numbers[i]
    previousNumbers = numbers[ i-25 : i ]

    if not isValidNumber(number, previousNumbers):
        invalidNumber = number
        break

print(invalidNumber)

print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

numbersInCount = set()
numberCount = 0
matchFound = False

for i in range(len(numbers)):
    # start new sequence
    for j in range(i, len(numbers)):
        # check next number in sequence
        numberCount += numbers[j]
        numbersInCount.add(numbers[j])

        if numberCount == invalidNumber:
            # found our sequence!
            matchFound = True
            break
        elif numberCount > invalidNumber:
            # sequence invalid: sum is too large
            numbersInCount = set()
            numberCount = 0
            break

    if matchFound:
        break

smallNumber = min(numbersInCount)
largeNumber = max(numbersInCount)
print('{} + {} = {}'.format(smallNumber, largeNumber, smallNumber + largeNumber))
