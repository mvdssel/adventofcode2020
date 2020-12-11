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

def executeCode(code):
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
        
        continueCode = \
            pointer >= 0 and \
            pointer < len(code) and \
            (not codeExecuted[pointer])
    
    # Return accumulator as result
    if pointer >= len(code):
        return (acc, True)
    else:
        return (acc, False)

print(executeCode(code))

print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

for i in range(len(code) -1, 0, -1):
    (operation, argument) = code[i]

    if operation == 'jmp':
        # take a COPY of the code
        codeCopy = list(code)
        # adjust one operation
        codeCopy[i] = ('nop', argument)
        # test it out
        (acc, success) = executeCode(codeCopy)
        if success:
            print('acc = ', acc, ' | operation ', i, ': ', operation, ' -> nop')

    elif operation == 'nop':
        # take a COPY of the code
        codeCopy = list(code)
        # adjust one operation
        codeCopy[i] = ('jmp', argument)
        # test it out
        (acc, success) = executeCode(codeCopy)
        if success:
            print('acc = ', acc, ' | operation ', i, ': ', operation, ' -> nop')

    # else: do nothing and go to next iteration
