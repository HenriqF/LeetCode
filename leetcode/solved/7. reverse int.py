#https://leetcode.com/problems/reverse-integer/description/

x= -12
ans = 0
if x < 0:
    a = list(map(int, str(-x)))
    b = [0] * len(a)
    for i in range(len(a)):
        b[i] = a[(len(a)- 1)-i]
    ans = -int(''.join(map(str, b)))        
else:
    a = list(map(int, str(x)))
    b = [0] * len(a)
    for i in range(len(a)): 
        b[i] = a[(len(a)-1)-i]
    ans = int(''.join(map(str, b)))
if ans > 2147483647 or ans < -2147483648:
    print(0)
else:
    print(ans) 