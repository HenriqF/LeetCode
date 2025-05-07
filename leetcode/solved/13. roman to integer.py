# https://leetcode.com/problems/roman-to-integer/
s = "MMMCMXCIX"
b = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
c = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
out = 0

for key in c:
    if key in s:
        out += c[key]
        s=s.replace(key,"")
for i in s:
    if i in b:
        out+=b[i]
print(out)




# p = 0
# while p < len(s):
#     t = ""
#     if p+1 < len(s):
#         t = ''.join([s[p], s[p+1]])
#     if t in c:
#         print(c[t])
#         out += c[t]
#         p += 1
#     else:
#         print(b[s[p]])
#         out += b[s[p]]
#     p+=1
# print(out)