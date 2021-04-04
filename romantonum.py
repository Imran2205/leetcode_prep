rom = 'MCMXCIV'
roman_dict = {
    'M': 1000,
    'D': 500,
    'C': 100,
    'L': 50,
    'X': 10,
    'V': 5,
    'I': 1,
    '': 0
}
rom = rom[::-1]
num = 0
prev_rom = 0
for i in range(len(rom)):
    if roman_dict[rom[i]] < prev_rom:
        num = num - roman_dict[rom[i]]
    else:
        num = num + roman_dict[rom[i]]
    prev_rom = roman_dict[rom[i]]
print(num)