#https://leetcode.com/problems/minimum-index-of-a-valid-split/description/
nums = [2,1,3,1,1,1,7,1,2,1]
l = len(nums)
p1 = {}
p2 = {}
for i in range(l):
    if nums[i] not in p2:
        p2[nums[i]] = 1
        p1[nums[i]] = 0
    else:
        p2[nums[i]] += 1

pos = 0
for num in nums:
    pos += 1
    p1[num] += 1
    p2[num] -= 1
    if p1[num] > (pos/2) and p2[num] > ((l-pos)/2):
        print(pos-1)
print(-1)


# def find(nums): #algoritmo legal para achar dominante
#     atual = 0
#     count = 0
#     for num in nums:
#         if num == atual:
#             count += 1
#         else:
#             if count == 0:
#                 atual = num
#             else:
#                 count -= 1
#     return atual