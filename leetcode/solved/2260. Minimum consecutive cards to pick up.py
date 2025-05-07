#https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/description/
cards = [3,4,2,3,4,7]
seen = {}
found = False
minil = 0
for i in range(0, len(cards)):
    if cards[i] not in seen:
        seen[cards[i]] = i
    else:
        if found == False:
            minil = (i - seen[cards[i]]+1)
            found = True
        
        minil = min(minil, i - seen[cards[i]]+1)
        seen[cards[i]] = i
if found == False:
    print(-1)
else:
    print(minil)