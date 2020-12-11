import re

INPUT = '02/input1.txt'

input = list()
passwords = list()

with open(INPUT) as f:
    input = f.read().splitlines()

for line in input:
    matchObj = re.match(r'(\d+)-(\d+) (\w): (\S+)', line)

    passwords.append({
        'minOcc': int(matchObj.group(1)),
        'maxOcc': int(matchObj.group(2)),
        'letter': matchObj.group(3),
        'password': matchObj.group(4)
    })

print()
print("------------------------------------------")
print("          PUZZEL 1")
print("------------------------------------------")
print()

validPasswords = list()
for password in passwords:
    pattern = r'[^' + password.get('letter') +']' 
    enkelletters = re.sub(pattern, '', password.get('password'))
    if(len(enkelletters) >= password.get('minOcc') and len(enkelletters) <= password.get('maxOcc')):
        validPasswords.append(password)

print('Amount of valid passwords: ', len(validPasswords))

print()
print("------------------------------------------")
print("          PUZZEL 2")
print("------------------------------------------")
print()

validPasswords = list()
for password in passwords:
    if(
        (password.get('password')[password.get('minOcc') - 1] == password.get('letter')) ^
        (password.get('password')[password.get('maxOcc') - 1] == password.get('letter'))
    ):
        validPasswords.append(password)

print('Amount of valid passwords: ', len(validPasswords))