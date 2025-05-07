#https://leetcode.com/problems/missing-number/description/

nums = [3,0,1]
res = len(nums)
res = (1 + res)*res // 2 
res = res - sum(nums)

print(res)
