#https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

stack = []
ops = {"+","-","/","*"}
for token in tokens:
    if token not in ops:
        stack.append(int(token))
    else:
        b = stack.pop()
        a = stack.pop()
        if token == "+":
            stack.append(a+b)
        elif token == "-":
            stack.append(a-b)
        elif token == "*":
            stack.append(a*b)
        else:
            stack.append(int(a/b))

print(stack[0])