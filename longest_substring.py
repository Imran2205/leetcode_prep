#s = "aabaab!bb"
s = "pwwkew"
s = "aabaab!bb"
current = ''
max_leng = 0
leng = 0
sub_s = ''
ptr = 0
while ptr < len(s):
    current = s[ptr]
    if current not in sub_s:
        leng = leng + 1
        sub_s = sub_s + current
        prev = current
        ptr = ptr + 1
    else:
        if leng > max_leng:
            max_leng = leng
        #ptr = ptr-len(sub_s)+1+sub_s.index(current)
        tot_len = len(sub_s)
        sub_s = sub_s[sub_s.index(current)+1:]
        leng = len(sub_s)
        #ptr = ptr + 1
if leng > max_leng:
    max_leng = leng
print(max_leng)
