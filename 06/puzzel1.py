import re 
import math 

INPUT = '06/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

questionCount = 0

# init loop
questions = set()
line = inputFile.readline()

while line:
    line = line.strip()

    if line != '':
        # still reading questions from the same group
        for question in line:
            questions.add(question)
    else:
        # starting new group
        questionCount += len(questions)
        questions = set()

    # prep next loop iteration
    line = inputFile.readline()

# postprocess loop
questionCount += len(questions)


print(questionCount)