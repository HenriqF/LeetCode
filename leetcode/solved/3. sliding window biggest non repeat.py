#https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

s = "abcabcbbadsfffgasdoitudo"
l = 0
seen = []
maior = 0

for r , char in enumerate(s):
    while char in seen:
        seen.remove(s[l])
        l += 1
    maior = max(maior, r-l+1)
    seen.append(char)

print(maior)