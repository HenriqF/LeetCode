#https://leetcode.com/problems/string-to-integer-atoi/description/

s = " -1010023630o4"
length = len(s)

index = 0
start = 0

while index < length and s[index].isspace():
    index += 1
if index == length:
    print(0)

start = index
if s[index] == "-" or s[index] == "+":
    sign = s[index]
    index += 1

while index < length and s[index].isdigit():
    index+=1

out = s[start:index]
print(out)


maxi = 2147483647
mini = -2147483648
try:
    num = int(out)
    print(max(min(num,maxi),mini))
except:
    print(0)
