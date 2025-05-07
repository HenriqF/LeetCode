# https://leetcode.com/problems/group-anagrams/description/

strs = ["eat","tea","tan","ate","nat","bat"]
mirror = {}
out = []

for i in range(0, len(strs)):
    e = ''.join(sorted(strs[i]))
    if e not in mirror:
        mirror[e] = []
    mirror[e].append(strs[i]) 

for key in mirror:
    out.append(mirror[key])

print(out)  
