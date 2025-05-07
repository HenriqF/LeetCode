#https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
number = "123"
digit = "3"
maxi = 0
for i in range(len(number)):
    if number[i] == digit:
        temp = int(number[:i]+number[i+1:])
        maxi = max(maxi, temp)

print(str(maxi))