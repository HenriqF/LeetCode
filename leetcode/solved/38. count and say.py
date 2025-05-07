#https://leetcode.com/problems/count-and-say/

def countandsay(n):
    if n == 1:
        return("1")
    elif n == 2:
        return("11")
    s = "11"
    for i in range(3, n+1):
        s += ' '
        leng = len(s)
        c = 1
        tmp = ""
        for j in range(1, leng):
            if s[j] != s[j-1]:
                tmp += str(c)
                tmp += s[j-1]
                c = 1
            else:
                c += 1
        s = tmp
    return s
            

print(countandsay(4))