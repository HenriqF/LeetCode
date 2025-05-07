#https://leetcode.com/problems/longest-common-prefix/description/

strs = ["flouw","fight","flower"]
size = (len(min(strs, key=len)))
prefix = strs[0][:size]

for i in range(0, len(strs)):
    strs[i] = strs[i][:size] 
    while strs[i] != prefix:
        if prefix == "":
            break
        strs[i] = (strs[i][:size])
        prefix = (prefix[:size])
        if strs[i] == prefix:
            break
        size -= 1
        print(prefix)

