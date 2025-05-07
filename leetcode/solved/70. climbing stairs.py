#https://leetcode.com/problems/climbing-stairs/description/
import time

#parece seguir fibonacci
n = 60
s = [1,1]
ans = 0
for i in range(0, n):
    if i % 2 == 0:
        s[0] = s[0]+s[1]
        ans = s[1]
    else:
        s[1] = s[0]+s[1]
        ans = s[0]
print(ans)
#caralho era realmente fibonacci wtf kkkk lets go sigma balls boys, ainda peguei 100% no tempo lets go im not the father wat the fuck i am such very goated and etcetera also i have type 4 diahorrea and also i do not know what a esternocleidomastoideo (tambem nao sei como que eu acertei esse nome desgramado de primeira hj eu to on fire dormir é para bixas eu consigo ser assim fodasticosem dormir)