#https://leetcode.com/problems/remove-element/description/

nums = [3,2,2,3]
val = 3
i = 0
while i < len(nums):
    if nums[i] == val:
        nums.remove(val)
    else:
        i += 1
print(nums)