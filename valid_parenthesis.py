s = "[["
s = list(s)
ans = True
print(s)
if len(s) > 1:
    while len(s) > 0:
        counter = 0
        while counter < len(s):
            if s[counter] == ')':
                if counter == 0:
                    ans = False
                    break
                elif s[counter - 1] == '(':
                    del s[counter]
                    del s[counter - 1]
                    break
                else:
                    ans = False
                    break
            elif s[counter] == ']':
                if counter == 0:
                    ans = False
                    break
                elif s[counter - 1] == '[':
                    del s[counter]
                    del s[counter - 1]
                    break
                else:
                    ans = False
                    break
            elif s[counter] == '}':
                if counter == 0:
                    ans = False
                    break
                elif s[counter - 1] == '{':
                    del s[counter]
                    del s[counter - 1]
                    break
                else:
                    ans = False
                    break
            if s[counter] == '(':
                if counter >= len(s) - 1:
                    ans = False
                    break
                elif s[counter + 1] == ')':
                    del s[counter + 1]
                    del s[counter]
                    break
                else:
                    counter = counter + 1
            elif s[counter] == '[':
                if counter >= len(s) - 1:
                    ans = False
                    break
                elif s[counter + 1] == ']':
                    del s[counter + 1]
                    del s[counter]
                    break
                else:
                    counter = counter + 1
            elif s[counter] == '{':
                if counter >= len(s) - 1:
                    ans = False
                    break
                elif s[counter + 1] == '}':
                    del s[counter + 1]
                    del s[counter]
                    break
                else:
                    counter = counter + 1
            else:
               counter = counter + 1
        print(s)
        if ans is False:
            break
else:
    ans = False

print(ans)