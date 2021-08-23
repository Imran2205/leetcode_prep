s = "PP"
num_rows = 1
out_put_str = ''
if len(s) > num_rows and num_rows > 1:
    for j in range(1, num_rows+1):
        i = j - 1
        strs = s[j-1]
        k = 1
        while i < len(s):
            i = i + 1
            if j == 1  or j == num_rows:
                i = i + (num_rows - 1) + (num_rows - 2)
                if i >= len(s):
                    break
                strs = strs + s[i]
            else:
                if k % 2 != 0:
                    i = i + (num_rows - j) + (num_rows - j - 1)
                    if i >= len(s):
                        break
                    strs = strs + s[i]
                else:
                    i = i + (((num_rows - 1) + (num_rows - 2)) - ((num_rows - j) + (num_rows - j - 1)) - 1)
                    if i >= len(s):
                        break
                    strs = strs + s[i]
            k = k + 1
        out_put_str = out_put_str + strs
else:
    out_put_str = s
print(out_put_str)

