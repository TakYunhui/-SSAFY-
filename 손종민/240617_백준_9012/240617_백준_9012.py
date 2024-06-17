# 9012 괄호

# 빈 스택을 만들어서
# (일 경우 일단 넣기
# 짝 맞는 )가 들어갈 경우 팝하기
# 스택에 남는 게 있으면 No, 없으면 YES

import sys

sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    case = input()
    stack = []  # 빈 리스트로 스택 만들기
    for i in case:
        if i == '(':
            stack.append(i)                     # 항목이 (면 일단 추가
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':      # 스택길이가 0이 아니고 직전 항목이 '('면 팝하기
                stack.pop()
            elif len(stack) == 0:                         # 받아오는 값이 )인 시점에서 스택 길이가 0일 경우 스택에 추가하고 break => 추가안하면 YES가 되어버림
                stack.append(i)
                break
            else: stack.append(i)                           # 스택 길이가 0이 아니면 일단 추가.. 지만 이럴 일은 없다고 보면 됨.

    if len(stack) == 0:
        print('YES')
    else : print('NO')
