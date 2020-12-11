import re

INPUT = '08/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

code = list()

# Read input file
for line in inputFile:
    pattern = r'(\w+) ([+-]\d+)'
    matchObj = re.match(pattern, line)

    operation = matchObj.group(1)
    argument = int(matchObj.group(2))

    code.append((operation, argument))

# Prep code execution
codeExecuted = [ False for i in range(len(code)) ]
continueCode = True
pointer = 0
acc = 0

# Execute code
while continueCode:
    (operation, argument) = code[pointer]
    codeExecuted[pointer] = True

    if operation == 'acc':
        acc += argument
        pointer += 1
    elif operation == 'jmp':
        pointer += argument
    elif operation == 'nop':
        pointer += 1
    else:
        raise Exception('invalid operation', operation)
    
    continueCode = not codeExecuted[pointer]

print(acc)