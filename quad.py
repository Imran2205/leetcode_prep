eq = input("equation:")
eq = str(eq)
numbers = []
sign_pos = []
sign = []
number_pos = []
power_pos = []
equ_pos = []
for i, x in enumerate(eq):
    if x == '^':
        power_pos.append(i+1)
    if x == '+' or x == '-':
        sign_pos.append(i)
    if x >= '0' and x <= '9':
        number_pos.append(i)
    if x == '=':
        equ_pos.append(i)
if sign_pos[0] != 0:
    sign_pos.insert(0, 0)
for i, x in enumerate(sign_pos):
    if eq[x] == '+':
        sign.append('+')
    elif eq[x] == '-':
        sign.append('-')
    else:
        sign.append('+')
numbers = []
i = 0
while i < len(number_pos):
    if number_pos[i] in power_pos:
        del number_pos[i]
    i = i + 1
i = 0
while i < len(number_pos):
    number = ''
    if i >= len(number_pos) - 1:
        break
    if number_pos[i+1] - number_pos[i] == 1:
        while number_pos[i+1] - number_pos[i] == 1:
            number = number + eq[number_pos[i]]
            i = i + 1
            if i >= len(number_pos) - 1:
                break
        number = number + eq[number_pos[i]]
        numbers.append(int(number))
    else:
        i = i + 1
if(len(numbers) > len(sign)):
    sign.append('+')
for i, x in enumerate(numbers):
    if(sign[i] == '+'):
        numbers[i] = x
    else:
        numbers[i] = x * -1
if len(equ_pos) > 0:
    if eq[equ_pos[0] + 1] != '0':
        numbers[-2] = numbers[-2] - numbers[-1]
        del numbers[-1]
print(numbers)


