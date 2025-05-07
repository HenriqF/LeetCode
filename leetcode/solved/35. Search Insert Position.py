#https://leetcode.com/problems/search-insert-position/description/
#o algoritmo de busca binaria é O(log n) 


nums = [1,4,5,7,10,24]
target = 7

l = 0
r = len(nums)-1

while l <= r:
    m = int((l+r)/2)
    if nums[m] > target:
        r = m-1
    elif nums[m] < target:
        l = m+1
    else:
        print(m)
print(l)
        