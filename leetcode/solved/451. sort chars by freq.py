#https://leetcode.com/problems/sort-characters-by-frequency/description/
s = "tree"
ans = ""
freq = {}

for char in s:
    if char not in freq:
        freq[char] = 1
    else:
        freq[char] += 1

freq = sorted(freq.items(), key=lambda item:item[1], reverse=True)
for i in freq:
    ans = ans + (i[0]*i[1])
print(ans)
