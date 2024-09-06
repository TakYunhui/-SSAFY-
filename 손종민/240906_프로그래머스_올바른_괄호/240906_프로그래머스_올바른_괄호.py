def solution(s):
    answer = True
    
    tmp_stack = []
    for word in s:
        # 스택이 비었고 '('면
        if not tmp_stack and word == '(':
            tmp_stack.append(word)
        elif not tmp_stack and word == ')':
            answer = False
            break
        elif tmp_stack and tmp_stack[-1] == '(':
            if word == ')':
                tmp_stack.pop()
            else:
                tmp_stack.append(word)
    if tmp_stack:
        answer = False
    return answer

s = "(())()"

print(solution(s))