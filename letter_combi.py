num_to_str = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

digits = '2379'
output = []
for d in digits:
    chrs = num_to_str[d]
    if len(output) == 0:
        output = chrs
    else:
        new_out = []
        for i in range(len(chrs)):
            for j in range(len(output)):
                new_out.append(chrs[i] + output[j])
        output = new_out
print(output)