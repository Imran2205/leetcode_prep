inp = "aswdf35342$#%$#hydsdasd"

out_str = ""
out_dict = {}

for i in inp:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        out_str = out_str + i
        if i in out_dict.keys():
            out_dict[i] = out_dict[i] + 1
        else:
            out_dict[i] = 1

print(out_str)

for j in out_dict.keys():
    out_print = '{} = {}'.format(j, out_dict[j])
    print(out_print)