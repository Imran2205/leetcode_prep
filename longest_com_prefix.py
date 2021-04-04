strs = ["flower","flow","flight"]

out = ""
matched = True
y = 0
if len(strs)<2:
    matched = False
    if len(strs) == 1:
        y = len(strs[0]) + 1


while matched:
    for x in range(len(strs) - 1):
        if y < len(strs[x]) and y < len(strs[x+1]):
            if strs[x][y] == strs[x+1][y]:
                matched = True
            else:
                matched = False
                break
        else:
            matched = False
            break
    y = y + 1

for i in range(y-1):
    out = out + strs[0][i]


print(out)