#https://leetcode.com/problems/binary-search/description/
nums = [-1,0,3,5,9,12]
target = 9

l = 0
h = len(nums)-1

while l <= h:
    m = l + (h-l)//2
    if nums[m] == target:
        print(m)
    elif nums[m] < target:
        l = m+1
    else:
        h = m-1
print("nao")
