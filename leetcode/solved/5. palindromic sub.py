import time
start_time = time.time()
# https://leetcode.com/problems/longest-palindromic-substring/description/

# FALHA! - tenho que fazer um algoritmo melhor (questao de tempo)

s = "jklfçasdfjklçaaaafaaaaafdsjklçfsadfhif"
sol = ""
m = 0

for i in range(0,len(s)):
    for j in range(1,len(s)):
        if s[i:j+1] == s[i:j+1][::-1]:
            e = len(s[i:j+1])
            if max(m, e) == e:
                m = e
                sol = s[i:j+1]
print("tempo:", time.time()-start_time, "seg")
print(len(sol))

