nums = [2,7,11,15]
target = 9
output = []
serial = list(range(0, len(nums)))
dicto = dict(zip(serial, nums))

#dicto = {}
#print(list(dicto.keys())[list(dicto.values()).index(5)])
for i in range(len(nums)):
    #dicto[i] = nums[i]
    res = target - nums[i]
    if res in dicto.values() and list(dicto.keys())[list(dicto.values()).index(res)] is not i:
        output.append(i)
        output.append(list(dicto.keys())[list(dicto.values()).index(res)])
        output.sort()
        break

print(output)