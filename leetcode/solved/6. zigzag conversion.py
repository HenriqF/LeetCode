#https://leetcode.com/problems/zigzag-conversion/description/
s = "carlosdealmeida"
numRows = 4
m = 1
current = 0
ansp = []

for char in s:
    a = []
    ansp.append(a)
    if current == numRows:
        m = -1
    elif current == 1:
        m = 1
    current += m
    ansp[current-1].append(char)
    
print(''.join(map(str, sum(ansp, []))))
