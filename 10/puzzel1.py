import re

INPUT = '10/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

# read adapter joltage
numbers = [ int(line) for line in inputFile ]
# add socket to the list
numbers.append(0)
# add device to the list
numbers.append(max(numbers) + 3)
# sort all numbers
numbers.sort()

oneCnt = 0
threeCnt = 0

for i in range(0, len(numbers) - 1):
    small = numbers[i]
    large = numbers[i+1]
    diff = large - small

    if diff == 1:
        oneCnt += 1
    elif diff == 3:
        threeCnt += 1
    elif diff > 3:
        print('{}: {} - {} = {}'.format(i, large, small, diff))
        break

print('{} -> {}'.format(1, oneCnt))
print('{} -> {}'.format(3, threeCnt))
print('{} x {} = {}'.format(oneCnt, threeCnt, oneCnt * threeCnt))


print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

# calculate valid jumps at each position
validNextAtNumber = dict.fromkeys(numbers)
for key in validNextAtNumber.keys():
    validNextAtNumber[key] = list()

for i in range(len(numbers)):
    # loop over potential numbers to skip to
    for j in range(i+1, len(numbers)):
        small = numbers[i]
        large = numbers[j]
        diff = large - small

        if diff <= 3:
                validNextAtNumber[small].append(large)
        else:
            break

# calulcate amount of options starting to count from certain position
# init empty list
optionsAtNumber = dict.fromkeys(numbers)

# init amount of options for last number in list (which is 1 option)
optionsAtNumber[numbers[-1]] = 1

# reverse traverse the list, skipping the last number
for number in reversed(numbers[0:-1]):
    options = 0

    for validNext in validNextAtNumber.get(number):
        options += optionsAtNumber.get(validNext)
    
    optionsAtNumber[number] = options

print(optionsAtNumber[0])
