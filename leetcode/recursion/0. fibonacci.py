def fibas(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibas(n-1) + fibas(n-2)


print(fibas(4))