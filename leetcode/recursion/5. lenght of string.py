def comp(str):
    if str == "":
        return 0
    return 1 + comp(str[1:])


print(comp("woddw"))