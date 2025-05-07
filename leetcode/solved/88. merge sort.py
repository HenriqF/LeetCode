#https://leetcode.com/problems/merge-sorted-array/description/
nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3

for i in range(n):
    nums1[m+i] = nums2[i]
nums1.sort()

print(nums1)
        