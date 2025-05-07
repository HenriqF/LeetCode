#https://leetcode.com/problems/pascals-triangle/description/
resp = [[1],[1,1]]
def pcal(numRows):
    if numRows == 1:
        return[[1]]
    elif numRows == 2:
        return[[1],[1,1]]
    else:
        for i in range(1,(numRows-1)):
            current = [1]
            leng = len(resp[i])
            leng = (leng-1)
            for j in range(0,(leng)):
                current.append((resp[i][j]+resp[i][j+1]))
            current.append(1)
            resp.append(current)
    return(resp)

print(pcal(13))