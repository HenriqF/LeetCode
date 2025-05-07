# https://leetcode.com/problems/top-k-frequent-elements/description/

nums = [1,1,1,2,2,3,4,4,4]
k = 2
seen = {}
out = []

for i in range(0, len(nums)):
    if nums[i] in seen:
        seen[nums[i]] += 1
    else:
        seen[nums[i]] = 0
    pass

# This is slower (provavelmente porque a funcao max seria O(n) no pior caso, assim, o tempo total final seria O(nk)... bem ruim.)
# for j in range(0,k):
#     e = max(seen, key = seen.get)
#     out.append(e)
#     seen[e] = -1
#     pass

# aparentemente organizar a lista é rapido pra porra/???
seen = sorted(seen.items(), key=lambda item:item[1], reverse=True)
for j,x in enumerate(seen[:k]): # isso seria bem rapido tbm
    out.append(x[0])

print(out)