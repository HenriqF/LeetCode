#https://leetcode.com/problems/counting-bits/description/
n=5
def countn(n):
    c = 0
    while n > 0:
        if n%2 == 1:
            c += 1
        n = n//2
    return c

ans = [0]
for i in range(1,n+1):
    ans.append(countn(i))

print(ans)