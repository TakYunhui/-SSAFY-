def solution(s):
    # stack 배열에 값 저장 후, 같은 값이 연속되게 나오면 제거... 아니면 뺐다가 다시 넣기
    stack = [s[0]]

    for i in range(1, len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    print(stack, len(stack))
    if len(stack):
        answer = 0
    else:
        answer = 1

    return answer