"""l1 = [0, 0, 0, 0, 9]
l2 = [0, 4, 0, 4]
number_1 = 0
number_2 = 0

multi = 1
for i in range(len(l1)):
    number_1 = number_1 + (multi * l1[i])
    multi = multi * 10

multi = 1
for i in range(len(l2)):
    number_2 = number_2 + (multi * l2[i])
    multi = multi * 10

number = number_1 + number_2

div = 10
out = []
print(number)
while int(number/div) != 0:
    out.append(number % div)
    number = int(number/div)

out.append(number % div)"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        number_1 = 0
        number_2 = 0
        multi = 1
        for i in range(len(l1)):
            number_1 = number_1 + (multi * l1[i])
            multi = multi * 10

        multi = 1
        for i in range(len(l2)):
            number_2 = number_2 + (multi * l2[i])
            multi = multi * 10

        number = number_1 + number_2
        div = 10
        out = []
        print(number)
        while int(number / div) != 0:
            out.append(number % div)
            number = int(number / div)

        out.append(number % div)
        return out

