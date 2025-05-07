#https://leetcode.com/problems/subsets/submissions/1570604222/

#minha solução (literalmente gozei, fiz em 6 minutos e deu certo de primeira slk oloco mds)
def subsets(arr):
    ans = []
    ans.append(arr)
    for num in arr:
        beta = arr[:]
        beta.remove(num)
        if len(beta) != 0:
            for set in subsets(beta):
                if set not in ans:
                    ans.append(set)
    return ans

a = subsets([1,2,3,4,5])
a.append([])
print(a)