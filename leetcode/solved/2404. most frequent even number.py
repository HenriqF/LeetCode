# https://leetcode.com/problems/most-frequent-even-element/description/
nums = [0,1,2,2,4,4,1]
seen = {}
sn = 0
oc = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        if nums[i] not in seen:
            seen[nums[i]] = 1
        else:
            seen[nums[i]] += 1
            
for value in seen:
    if seen[value] > oc:
        oc = seen[value]
        sn = value
    elif seen[value] == oc:
        sn = min(sn, value)


if oc == 0:
    print("fake")
print(sn)