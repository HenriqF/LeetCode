#https://leetcode.com/problems/two-sum/
target = 6
nums = [3,3,4]
seen = {}

for num in enumerate(nums):
    if num[1] not in seen:
        seen[num[1]] = num[0]
        
for num in enumerate(nums):
    comp = target - num[1]
    if comp in seen:
        if seen[comp] != num[0]:
            print(seen[comp], num[0])
