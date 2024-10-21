# deque로 처리?
from collections import deque


def solution(s):
    s = deque(s)
    count = 0
    answer = 0
    while count < len(s):
        # 확인해보자
        print(s)

        # 임시 스택
        tmp = []
        for i in range(len(s)):
            # tmp가 비어있으면
            if not tmp:
                # 원소 추가
                tmp.append(s[i])
            # 안에 값이 있으면
            else:
                if s[i] == ')' and tmp[-1] == '(':
                    tmp.pop()
                elif s[i] == '}' and tmp[-1] == '{':
                    tmp.pop()
                elif s[i] == ']' and tmp[-1] == '[':
                    tmp.pop()
                else:
                    tmp.append(s[i])
            print(tmp)
        
        # for문 다 돌고 stack이 비어있으면
        if not tmp:
            answer += 1

        # 괄호 회전
        s.append(s.popleft())

        count += 1

    return answer


s = '[)(]'

print(solution(s))