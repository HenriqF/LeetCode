#https://leetcode.com/problems/longest-consecutive-sequence/description/
nums = [100,4,200,1,3,2]
seen = set(nums)
maxi = 0
for num in seen:
    if num - 1 not in seen:
        l = 1
        while num + l in seen:
            l += 1
        maxi = max(maxi, l)


print(maxi)
