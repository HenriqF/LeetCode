#https://leetcode.com/problems/permutations/description/
nums = [1,2,3,4]
def permutations(nums):
    ans = []
    if len(nums) <= 1:
        return([nums])
    for i in range(len(nums)):
        beta = nums[:]
        beta.pop(i)
        for subset in permutations(beta):
            ans.append([nums[i]]+subset)

    return ans

print(permutations(nums))