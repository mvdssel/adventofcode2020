import re 
import math 

INPUT = '06/input1.txt'

print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

result = 0

# init loop
questions = dict()
groupSize = 0

for line in inputFile:
    line = line.strip()

    if line != '':
        # still reading questions from the same group
        groupSize += 1
        for question in line:
            questions[question] = questions.get(question, 0) + 1
    else:
        # finalise previous group
        for question, questionCount in questions.items():
            if questionCount == groupSize:
                result += 1

        # reset for next group
        questions = dict()
        groupSize = 0

# postprocess loop
for question, questionCount in questions.items():
    if questionCount == groupSize:
        result += 1

print(result)
