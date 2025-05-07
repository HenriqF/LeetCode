#https://leetcode.com/problems/container-with-most-water/description/

height = [1,8,6,2,5,4,8,3,7]

l = 0
r = len(height)-1
water = 0


water = (min(height[l], height[r])*(r-l))
while l != r:
    if height[l] > height[r]:
        r -= 1
    else:
        l += 1
    water = max((min(height[l], height[r])*(r-l)), water)
print(water)
    