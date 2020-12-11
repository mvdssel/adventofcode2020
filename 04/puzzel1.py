import re 
INPUT = '04/input1.txt'

input = list()
with open(INPUT) as f:
    input = f.read().splitlines()

print(input)
print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")


Passports=[]    
NewPassport = ''

for line in input:
    if line !='': 
        NewPassport += ' ' + line
    else:
        Passports.append(NewPassport) 
        NewPassport= ''

Passports.append(NewPassport)

Str1 = 'byr:'
Str2 = 'iyr:'
Str3 = 'eyr:'
Str4 = 'hgt:'
Str5 = 'ecl:'
Str6 = 'pid:'
Str7 = 'hcl:'

count = 0

for line in Passports:
    if (line.find(Str1) > 0 
    and line.find(Str2) > 0
    and line.find(Str3) > 0
    and line.find(Str4) > 0
    and line.find(Str5) > 0
    and line.find(Str6) > 0
    and line.find(Str7) > 0):
        count+=1

print(count)

1+1


