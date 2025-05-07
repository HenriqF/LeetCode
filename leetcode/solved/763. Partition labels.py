#https://leetcode.com/problems/partition-labels/description/

s = "caedbdedda"
seen = {}

for i in range(len(s)):
    if s[i] not in seen:
        seen[s[i]] = [i,i]
    else:
        seen[s[i]][1] = i

out = []
current = seen[s[0]]

for key in seen:
    
    cmin, cmax = current
    nmin, nmax = seen[key]

    if nmin >= cmin and nmax <= cmax:
        pass
    elif nmax < cmin or nmin > cmax:
        out.append(current)
        current = seen[key]
    else:
        if nmax > cmax:
            current[1] = nmax
        elif nmin < cmin:
            current[0] = nmin

out.append(current)
for i in range(len(out)):
    out[i] = out[i][1] - out[i][0] +1

print(out)

    
