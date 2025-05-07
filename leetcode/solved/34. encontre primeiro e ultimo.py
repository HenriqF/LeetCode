#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

nums = [5,7,7,8,8,10]
target = 8
try:                               
    p = nums.index(target)         
    u = nums[::-1].index(target)  
    u = (len(nums)-1)-u   
    print([p, u])      
except:
    print([-1, -1]) 