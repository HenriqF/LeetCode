#https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

needle = "c"
haystack = "abc"

for i in range(len(haystack)-len(needle)+1):
    if haystack[i:i+len(needle)] == needle:
        print(i)

print(-1)