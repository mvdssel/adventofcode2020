import regex
import math 

INPUT = '07/input1.txt'

print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")

inputFile = open(INPUT, 'r')

canResideIn = dict()
bagContents = dict()

for line in inputFile:
    pattern = r'(\w+ \w+) bags? contain (((\d+) (\w+ \w+) bags?,? ?)+|no other bags?)'
    matchObj = regex.match(pattern, line)
    bigBag = matchObj.captures(1)[0]
    littleBagCount = matchObj.captures(4)
    littleBags = matchObj.captures(5)

    for i, littleBag in enumerate(littleBags):
        # init canResideIn
        if littleBag in canResideIn:
            canResideIn[littleBag].add(bigBag)
        else:
            canResideIn[littleBag] = set([bigBag])
        # init mustContain
        if bigBag in bagContents:
            bagContents[bigBag][littleBag] = int(littleBagCount[i])
        else:
            bagContents[bigBag] = { littleBag: int(littleBagCount[i]) }

canContainGoldBag = set()
toCheck = canResideIn.get('shiny gold')

while len(toCheck) != 0:
    bigBag = toCheck.pop()
    canContainGoldBag.add(bigBag)

    for biggerBag in canResideIn.get(bigBag, []):
        toCheck.add(biggerBag)

print(canContainGoldBag)
print(len(canContainGoldBag))

print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")

bagsInGoldenCount = 0
toCheck = [ bagContents.get('shiny gold') ]

while len(toCheck) != 0:
    goldenBagContents = toCheck.pop()

    for littleBag, littleBagCount in goldenBagContents.items():
        bagsInGoldenCount += littleBagCount
        littleBagContents = bagContents.get(littleBag, {})

        additionalGoldenBagContents = dict()
        for tinyBag, tinyBagCount in littleBagContents.items():
            additionalGoldenBagContents[tinyBag] = tinyBagCount * littleBagCount
        
        toCheck.append(additionalGoldenBagContents)

print(bagsInGoldenCount)