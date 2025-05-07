#https://leetcode.com/problems/word-break/description
wordDict = ["car","ca","rs"]
s = "cars"

n = len(s)
dp = [False] * (n + 1)
dp[0] = True
max_len = max(map(len, wordDict))  

for i in range(1, n + 1):
    for j in range(i - 1, max(i - max_len - 1, -1), -1):
        if dp[j] and s[j:i] in wordDict:
            dp[i] = True
            break

print(dp[n])

#vai tomar no cu q q é isso