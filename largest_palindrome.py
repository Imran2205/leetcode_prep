s = "babaddtattarrattatddetartrateedredividerb"



"""if len(s) < 2:
    largest_palindrome = s
elif len(s) < 3:
    if s[0] == s[1]:
        largest_palindrome = s
    else:
        largest_palindrome = s[0]"""
#else:

def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True
def lar_par(s):
    #largest_palindrome = ''
    for i in range(len(s)):
        j = 0
        while j+(len(s)-i-1) < len(s):
            sub_s = s[j:j+(len(s)-i)]
            j = j + 1
            if sub_s[0] == sub_s[-1]:
                if isPalindrome(sub_s):
                    # if len(sub_s) > len(largest_palindrome):
                    # largest_palindrome = sub_s
                    return sub_s

    return ''



print(lar_par(s))






