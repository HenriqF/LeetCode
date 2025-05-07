#https://leetcode.com/problems/product-of-array-except-self/description/
# Solução dos dois triangulos:
# [1,2,3,4]      [1,2,3,4] | Juntos:
#    1 1 1        2        | 2 1 1 1
#      2 2        3 3      | 3 3 2 2
#        3        4 4 4    | 4 4 4 3
# Triangulo 1


# nums = [1,2,3,4]
# ans = [1] * len(nums)
# c=nums[0]
# for i in range(1,len(nums)):
#     ans[i] *= c
#     c *= nums[i]
# c=1
# print(ans)

# for j in range(len(nums)-2, -1, -1):
#     c *= nums[j+1]
#     ans[j] *= c
# print(ans)

# Solução caso podesse usar divisão:

nums = [-1,1,0,-3,3]
prod = 1
c = False
for num in nums:
    if num != 0:
        prod *= num
    else:
        c = True

for i in range(len(nums)):
    if c == False:
        if nums[i] != 0:
            nums[i] = int(prod/nums[i])
    else:
        if nums[i] == 0 and prod != 1:
            nums[i] = int(prod)
        else:
            nums[i] = 0

print(nums)