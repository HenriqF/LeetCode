#https://leetcode.com/problems/sliding-window-maximum/description/

nums = [9,11]
k = 2

queue = []
out = []

if k == 1:
    print(nums)

for i in range(len(nums)):
    num = nums[i]
    while queue != [] and num > queue[-1]:
        queue.pop(-1)
    queue.append(num)
    if i >= k and nums[i-k] == queue[0]:
        queue.pop(0)
    if i >= k-1:
        out.append(queue[0])
print(out)
#nesse caso, usa-se o deque para deixar 100% bala
# from collections import deque
# queue = deque()
# out = []
# if k == 1:
#     print(nums)

# for i in range(len(nums)):
#     num = nums[i]
#     while queue and num > queue[-1]:
#         queue.pop()
#     queue.append(num)
#     if i>= k and nums[i-k] == queue[0]:
#         queue.popleft()
#     if i >= k-1:
#         out.append(queue[0])
# print(out)

#se nao tivesse limite de tempo:
# out = []

# for i in range(0, len(nums)-k+1):
#     out.append(max(nums[i:k+i]))

# return(out)