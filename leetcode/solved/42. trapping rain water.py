# https://leetcode.com/problems/trapping-rain-water/description/

# achar forma mais rapida

# # height = [2,1,0,1,3,2]
# max = max(height)
# current = max
# total = 0

# for i in range(1 ,max+1):
#     l = 0
    
#     for r in range(0, len(height)-1):
#         stop = False
#         if height[r] >= current and height[r+1] < current:
#             l = r+1
#             while height[l] < current:
#                 if l == len(height)-1:
#                     stop = True
#                     break
#                 l += 1
#             if height[r] >= current and height[l] >= 0 and stop == False:
#                 total += l-r-1
#     current -= 1

# print(total)

height = [2,1,0,1,3,2]

maxl = height[0]
maxr = height[len(height)-1]
l = 0
r = len(height)-1
total = 0

while l < r:
    if maxr > maxl:
        l += 1
        maxl = max(maxl, height[l])
        total += maxl - height[l]
    else:
        r -= 1
        maxr = max(maxr, height[r])
        total += maxr - height[r]

print(total)