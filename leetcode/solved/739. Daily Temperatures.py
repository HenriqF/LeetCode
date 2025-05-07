#https://leetcode.com/problems/daily-temperatures/description/
temperatures = [73,74,75,71,69,72,76,73]
answer = [0] * len(temperatures)

stack = []

for i in range(0, len(temperatures)):
    while stack and temperatures[i] > temperatures[stack[-1]]:
        pos = stack.pop()
        answer[pos] = i-pos
    stack.append(i)

print(answer)
