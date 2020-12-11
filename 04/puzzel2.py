import re 
INPUT = '04/input1.txt'

input = list()
with open(INPUT) as f:
    input = f.read().splitlines()

# print(input)
print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")


# Read all passports
strPassports=[]    
strPassport = ''

for line in input:
    if line !='': 
        strPassport += ' ' + line
    else:
        strPassports.append(strPassport) 
        strPassport= ''
strPassports.append(strPassport)

# Parse all passports
passports = list()

for strPassport in strPassports:
    passport = dict()

    passportAttributes = strPassport.strip().split(' ')
    passportAttributes = list(map(lambda attr: attr.split(':'), passportAttributes))

    for attr in passportAttributes:
        passport[attr[0]] = attr[1]

    passports.append(passport)


def validateByr(byr):
    if(
        int(byr) >= 1920 and int(byr) <= 2002 and
        len(byr) == 4
    ):
        return True
    else:
        return False

def validateIyr(iyr):
    if(
        int(iyr) >= 2010 and int(iyr) <= 2020 and
        len(iyr) == 4
    ):
        return True
    else:
        return False

def validateEyr(eyr):
    if(
        int(eyr) >= 2020 and int(eyr) <= 2030 and
        len(eyr) == 4
    ):
        return True
    else:
        return False

def validateHgt(hgt):
    pattern = r'^(\d+)(cm|in)$'

    matchObj = re.match(pattern, hgt)

    if matchObj != None:
        value = int(matchObj.group(1))
        unit = matchObj.group(2)

        if (unit == 'cm'
            and value >= 150 and value <= 193
        ):
            return True

        elif (unit == 'in'
            and value >= 59 and value <= 76
        ):
            return True

    return False

def validateHcl(hcl):
    pattern = r'^#[\da-f]{6}$'

    matchObj = re.match(pattern, hcl)

    if matchObj != None:
        return True

    return False

def validateEcl(ecl):
    validColors = set([
        'blu',
        'amb',
        'brn',
        'gry',
        'grn',
        'hzl',
        'oth'
    ])

    return ecl in validColors

def validatePid(pid):
    pattern = r'^\d{9}$'

    matchObj = re.match(pattern, pid)

    if matchObj != None:
        return True

    return False

count = 0
for passport in passports:
    byr = passport.get('byr')
    iyr = passport.get('iyr')
    pid = passport.get('pid')
    eyr = passport.get('eyr')
    hgt = passport.get('hgt')
    hcl = passport.get('hcl')
    ecl = passport.get('ecl')

    if(
        byr != None and
        iyr != None and
        eyr != None and
        hgt != None and
        hcl != None and
        ecl != None and
        pid != None and
        validateByr(byr) and
        validateIyr(iyr) and
        validateEyr(eyr) and
        validateHgt(hgt) and
        validateHcl(hcl) and
        validatePid(pid) and
        validateEcl(ecl)
    ):
        count += 1

print('Valid passports: ', count)


# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.