# https://leetcode.com/problems/contains-duplicate/description/
nums = [1,2,3,4,4,5,6,7]

seen = {}
nums = sorted(nums)

for i in range(0,(len(nums)-1)):
    if nums[i] == nums[i+1]:
        print("True")
print("false")


#     if nums[i] not in seen:
#         seen[nums[i]] = 0
#     else:
#         print("true")
# print("false")


print((len(set(nums))) < len(nums))