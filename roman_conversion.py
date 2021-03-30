num = 1994

roman_dict = {
    1000: 'M',
    500: 'D',
    100: 'C',
    50: 'L',
    10: 'X',
    5: 'V',
    1: 'I',
    0: ''
}
out = ''
keys = list(roman_dict.keys())
lp = 0
divider = keys[lp]
while divider > 0:
    res = num // divider
    rem = num % divider
    if lp % 2 != 0 and res == 1:
        lp = lp + 1
        divider = keys[lp]
        num = rem
        res = num // divider
        rem = num % divider
        if res == 4:
            out = out + roman_dict[divider]
            out = out + roman_dict[keys[lp-2]]
            num = rem
            lp = lp + 1
            divider = keys[lp]
        else:
            out = out + roman_dict[keys[lp-1]]
            for i in range(res):
                out = out + roman_dict[divider]
            num = rem
            lp = lp + 1
            divider = keys[lp]
    else:
        if res == 4:
            out = out + roman_dict[divider]
            out = out + roman_dict[keys[lp - 1]]
        else:
            for i in range(res):
                out = out + roman_dict[divider]
        num = rem
        lp = lp + 1
        divider = keys[lp]

print(out)
