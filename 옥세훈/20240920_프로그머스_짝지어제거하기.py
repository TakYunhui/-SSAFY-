def solution(s):
    s = list(s)
    stack = []
    for i in range(len(s)):

        if not stack:
            stack.append(s[i])
            continue

        top = stack[-1]
        if top == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        return 0

    return 1