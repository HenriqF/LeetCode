#https://leetcode.com/problems/generate-parentheses/description/

def genpar(n):
    res = []

    def busca(o, c, s):
        if o == c and o + c == n*2:
            res.append(s)
            return
        if o < n:
            busca(o+1, c, s + "(")
        if c < o:
            busca(o, c+1, s+")")
    
    busca(0, 0, "")
    return res

print(genpar(10))