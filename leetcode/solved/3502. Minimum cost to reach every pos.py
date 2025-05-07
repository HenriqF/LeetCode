#https://leetcode.com/problems/minimum-cost-to-reach-every-position/


cost = [5,3,4,1,3,2]
for i in range(0, len(cost)-1):
    if cost[i+1] > cost[i]:
        cost[i+1] = cost[i]

print(cost)
                