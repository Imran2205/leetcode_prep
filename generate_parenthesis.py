n = 8
def gen_par(n):
    parr_arr = []
    for i in range(1, n+1):
        parr_str11 = ''
        parr_str12 = ''
        for x in range(i):
            parr_str11 = parr_str11 + '('
            parr_str12 = parr_str12 + ')'
        parr_str1 = parr_str11 + parr_str12
        parr_str21 = ''
        parr_str22 = ''
        for x in range(n-i):
            parr_str21 = parr_str21 + '('
            parr_str22 = parr_str22 + ')'
        parr_str2 = parr_str21 + parr_str22
        parr_out = parr_str1 + parr_str2
        parr_arr.append(parr_out)
        print([i, n-i])
        if i < n:
            l1 = gen_par(i)
            l2 = gen_par(n - i)
            for el1 in l1:
                for el2 in l2:
                    f_el = el1 + el2
                    parr_arr.append(f_el)
                    if i == 1:
                        f_el = '(' + el2 + ')'
                        parr_arr.append(f_el)
    return parr_arr

out = gen_par(n)
out = list(dict.fromkeys(out))
print(out)

