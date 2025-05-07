ratings = [2,3,5,5,4,1]
l = len(ratings)
total = l

i = 1
while i < l:
    if ratings[i] == ratings[i-1]:
        i += 1
        continue
    peak = 0
    while i<l and ratings[i] > ratings[i-1]:
        peak += 1
        total += peak
        i += 1
    if i == l:
        print(total)
    valley = 0
    while i < l and ratings[i] < ratings[i-1]:
        valley += 1
        total += valley
        i += 1
    total -= min(peak, valley)


print(total)