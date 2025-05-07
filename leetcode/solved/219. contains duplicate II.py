nums = [1,0,1,1,0,0,1]
k = 5
seen = {}

for i in range(0, len(nums)):
    if nums[i] in seen:
        if abs(i - seen[nums[i]]) <= k:            
            print("true")
    seen[nums[i]] = i
    print(seen)
print("false")

        #https://leetcode.com/problems/contains-duplicate-ii/submissions/1507858436/?source=submission-noac
        # for i in range(0, len(nums)):
        #     if nums[i] not in seen:
        #         seen[nums[i]] = i
        #     else:
        #         if abs(i - seen[nums[i]]) <= k:
        #             return True
        # return False