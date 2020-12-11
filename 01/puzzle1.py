INPUT = '01/input1.txt'

input = list()

with open(INPUT) as f:
    input = f.read().splitlines()

input = set(map(lambda x: int(x), input))

print(input)
print()
print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")
print()

for getalleke in input:
    rest = 2020 - getalleke

    if rest in input:
        print("Gevonden: {} en {}".format(getalleke, rest))
        print("{} + {} = {}".format(getalleke, rest, getalleke + rest))
        print("{} x {} = {}".format(getalleke, rest, getalleke * rest))
        break

print()
print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")
print()

gevonden = False
for getalleke in input:
    for andergetalleke in input:
        rest = 2020 - getalleke - andergetalleke
        
        if rest in input:
            print("Gevonden: {} en {} en {}".format(getalleke, andergetalleke, rest))
            print("{} + {} + {} = {}".format(
                getalleke,
                andergetalleke,
                rest,
                getalleke + andergetalleke +  rest))
            print("{} x {} x {} = {}".format(
                getalleke,
                andergetalleke,
                rest,
                getalleke * andergetalleke * rest))
            gevonden = True
            break
    
    if gevonden:
        break
