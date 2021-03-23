import numpy as np
s = "abcd"
p = "ab*cd"
len_s = len(s)
len_p = len(p)

sol = [[False for i in range(len_p+1)] for j in range(len_s+1)]

sol[0][0] = True

for j in range(1, len_p+1):
    if p[j-1] == '*':
        sol[0][j] = sol[0][j-2]

for i in range(1, len_s+1):
    for j in range(1, len_p+1):
        if s[i-1] == p[j-1] or p[j-1] == '.':
            sol[i][j] = sol[i-1][j-1]
        elif p[j-1] == '*':
            if s[i-1] == p[j-2] or p[j-2] == '.':
                sol[i][j] = sol[i][j-1] or sol[i-1][j] or sol[i][j-2]
            else:
                sol[i][j] = sol[i][j-2]


print(sol[len_s][len_p])
#sol[len_s][len_p] = True


"""for j in range(len_p, 0, -1):
    if p[j-1] == '*':
        sol[len_s][j-2] = sol[len_s][j]

for i in range(len_s, 0, -1):
    for j in range(len_p, 0, -1):
        if s[i-1] == p[j-1] or p[j-1] == '.':
            sol[i-1][j-1] = sol[i][j]
        elif p[j-1] == '*':
            if s[i-1] == p[j-2] or p[j-2] == '.':
                sol[i-1][j-1] = sol[i-1][j+1]
            else:
                sol[i-1][j-1] = sol[i-1][j] or sol[i][j-1] or sol[i-1][j+1]

print(np.array(sol[0][0]))"""


