l1 = [0,1,2,3]
l2 = [2,3,4,5]

lst = l1 + l2
lst.sort()

lng = len(lst)
if(lng % 2 == 0):
    median = (lst[lng//2 - 1] + lst[lng//2]) / 2
else:
    median = lst[lng//2]

print(median)