# https://leetcode.com/problems/majority-element/description/

nums = [2,2,1,1,1,2,2,1,1]
dict = {}
n = len(nums)

for i in range(n):
    if nums[i] not in dict:
        dict[nums[i]] = 0
    dict[nums[i]] += 1
    if dict[nums[i]] >= (n/2):
        print(nums[i])

