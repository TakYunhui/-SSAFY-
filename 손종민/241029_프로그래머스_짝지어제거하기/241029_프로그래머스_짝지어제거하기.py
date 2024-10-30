from collections import deque

def solution(s):
    stack = []
    s = deque(s)
    while s:
        this_one = s.popleft()
        # 스택이 비어있으면 혹은 짝이 안맞으면
        if not stack or stack[-1] != this_one:
            # 쌓고
            stack.append(this_one)
        # 짝이 맞으면 팝
        else:            
            stack.pop()

    if stack:    
        return 0
    else:
        return 1


s = 'cdcd'

print(solution(s))