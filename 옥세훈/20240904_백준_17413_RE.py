import sys


s = sys.stdin.readline().strip() + ' '

# print(s)

flag = False
stack = []
result = ""
for i in s:
    if i == "<":
        flag = True
        for _ in range(len(stack)):
            result += stack.pop()
    stack.append(i)

    if i == ">":
        flag = False
        for _ in range(len(stack)):
           result += stack.pop(0)

    if i == ' ' and not flag:
        stack.pop()
        for _ in range(len(stack)):
            result += stack.pop()
        result += ' '

print(result)

