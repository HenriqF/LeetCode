#https://leetcode.com/problems/string-compression/description/
chars = ["a","a","b","b","c","c","c"]

#Espaco constante, rápido até
chars.append("skendel")
count = 1

i = 0
j = 1
b = 0

while i < len(chars)-1:
    while chars[j] == chars[i] and j < len(chars)-1:
        count += 1
        j += 1
    else:
        chars[b] = chars[i]
        b+=1
        if count > 1:
            for char in str(count):
                chars[b] = char
                b+=1
        count=0
        i=j
print(chars)


#Not constant extra space, very fast O(n):
# s = []

# count = 1
# chars.append(" ")
# for i in range(1, len(chars)):
#     if chars[i] == chars[i-1]:
#         count += 1
#     else:
#         s.append(chars[i-1])
#         if count > 1:
#             s.extend(str(char) for char in str(count))

#         count = 1

# chars = s
# print(chars)
# print(len(chars))
