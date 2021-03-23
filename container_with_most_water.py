height = [4,3,2,1,4]

"""for i in range(len(height)):
    for j in range(len(height[0:i+1])):
        h = min([height[i], height[j]])
        w = abs(i-j)
        a = h*w
        area.append(a)
print(max(area))"""

area = 0
for i in range(len(height)):
    for j in range(len(height[0:i+1])):
        h = min([height[i], height[j]])
        w = abs(i-j)
        a = h*w
        if a>area:
            area = a
print(area)