# https://leetcode.com/problems/valid-parentheses/description/

s = "{{}}"
map = {")":"(","]":"[","}":"{"}
stack = []

for char in s:
    if char in map.values():
        stack.append(char)
    elif char in map.keys():
        if not stack:
            print(False)
        elif map[char] != stack.pop():
            print(False)
print(not stack)

# for char in s:
#     if char in map.values():
#         stack.append(char)
#     elif char in map.keys():
#         if not stack or map[char] != stack.pop():
#             print("false")
#print(not stack) # caso stack estiver cheio, responde falso. Vice versa