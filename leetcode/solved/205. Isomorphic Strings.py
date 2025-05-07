s = "eggeg"
t = "geege"
# l = len(s)
# idxseen = {}

# if l != len(t):
#     print(False)

# for i in range(l):
#     chars = s[i]
#     chart = str(t[i])+"bazingen"

#     if chars not in idxseen and chart not in idxseen:
#         idxseen[chars] = i
#         idxseen[chart] = i
#     elif chars in idxseen and chart in idxseen:
#         idxseen[chars] += 1
#         idxseen[chart] += 1
#         if idxseen[chars] != idxseen[chart]:
#             print("FALSE")
#     else:
#         print("FALSE")

# print("true")


count1 = {}
count2 = {}

l1 = []
l2 = []

if len(s) != len(t):
    print(False)

for i in range(0,len(s)):
    if s[i] not in count1:
        count1[s[i]] = i
        l1.append(count1[s[i]])
    else:
        l1.append(count1[s[i]])

    if t[i] not in count2:
        count2[t[i]] = i
        l2.append(count2[t[i]])
    else:
        l2.append(count2[t[i]])
print(count1)
if l1 == l2:
    print(True)
print(False)