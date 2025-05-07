#https://leetcode.com/problems/sort-colors/description/

nums = [2,0,2,1,1,0]

out =[[],[],[]]
for num in nums:
    out[num].append(num)
out = (sum(out, []))
for i in range(len(out)):
    nums[i] = out[i]
print(nums)

# z = 0
# o = 0
# t = 0
# for num in nums:
#     if num == 0:
#         z += 1
#     elif num == 1:
#         o += 1
#     else:
#         t += 1

# c = 0
# for i in range(z):
#     nums[c] = 0
#     c += 1
# for i in range(o):
#     nums[c] = 1
#     c += 1
# for i in range(t):
#     nums[c] = 2
#     c += 1

# print(nums)