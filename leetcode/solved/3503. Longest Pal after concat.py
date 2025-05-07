#https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-i/description/
s = "abcde"
t = "ecdba"

length = 0
        
for i in range(len(s)+1):
    for j in range(i, len(s)+1):
        t1 = s[i:j]
        for k in range(len(t)+1):
            for m in range(k, len(t)+1):
                t2 = t1 + t[k:m]
                print(t2)
                if len(t2) > length and t2 == t2[::-1]:
                    length = len(t2)

print(length)