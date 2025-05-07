
def sum(arr):
    if len(arr) == 1:
        return arr[0]
    beta = arr.copy()
    beta.pop(0)
    return arr[0] + sum(beta)

print(sum([1,5,3]))



