# 1차풀이: 답이 너무 엉뚱함 -> 뭔가 문제 이해를 잘못한 거 같음
# def solution(prices):
#     answer = []
#     # 가격이 떨어지지 않는 기간을 계속 기록해야 함
#     # for문으로 한번씩만 보면 기록이 안 될듯?
#     stack = [prices[0]]
#     idx = 1
#     temp = 0
#
#     while len(answer) < len(prices):
#         prev = stack.pop()
#         current = prices[idx]
#         if idx < len(prices):
#             if current > prev:
#                 stack.append(prev)
#                 stack.append(current)
#                 idx += 1
#                 print(f'current > prev: {idx, stack, answer, prev, current}')
#             else:
#                 answer.append(len(stack))
#                 stack = [current]
#                 print(f'else: {idx, stack, answer, prev, current}')
#
#     return answer
'''
테스트 1
입력값 〉	[1, 2, 3, 2, 3]
기댓값 〉	[4, 3, 1, 1, 0]
실행 결과 〉	실행한 결괏값 [2,0,0,0,0]이 기댓값 [4,3,1,1,0]과 다릅니다.
출력 〉	current > prev: (2, [1, 2], [], 1, 2)
current > prev: (3, [1, 2, 3], [], 2, 3)
else: (3, [2], [2], 3, 2)
else: (3, [2], [2, 0], 2, 2)
else: (3, [2], [2, 0, 0], 2, 2)
else: (3, [2], [2, 0, 0, 0], 2, 2)
else: (3, [2], [2, 0, 0, 0, 0], 2, 2)
'''

#
# def solution(prices):
#     answer = []
#     # 가격이 떨어지지 않는 기간을 계속 기록해야 함
#     # for문으로 한번씩만 보면 기록이 안 될듯?
#     stack = [prices[0]]
#     idx = 1
#     tmp = len(prices)
#
#     while len(answer) < len(prices):
#         prev = stack.pop()
#         current = prices[idx]
#         if idx < len(prices):
#             print(idx)
#             if current > prev:
#                 stack.append(prev)
#                 stack.append(current)
#                 if idx + 1 < len(prices):
#                     idx += 1
#                 print(f'current > prev: {current, prev, idx, tmp, answer}')
#             else:
#                 tmp -= 1
#                 answer.append(tmp)
#                 stack = [current]
#                 print(f'else: {current, prev, idx, tmp, answer}')
#
#     return answer
'''
	[1, 2, 3, 2, 3]
기댓값 〉	[4, 3, 1, 1, 0]
실행 결과 〉	실행한 결괏값 [4,3,2,1,0]이 기댓값 [4,3,1,1,0]과 다릅니다.
출력 〉	1
current > prev: (2, 1, 2, 5, [])
2
current > prev: (3, 2, 3, 5, [])
3
else: (2, 3, 3, 4, [4])
3
else: (2, 2, 3, 3, [4, 3])
3
else: (2, 2, 3, 2, [4, 3, 2])
3
else: (2, 2, 3, 1, [4, 3, 2, 1])
3
else: (2, 2, 3, 0, [4, 3, 2, 1, 0])
'''
# 처음 n초에서 가격이 떨어진 시점에 -1하는 게 아니라, 가격이 떨어진 시간 자체를 세는 듯??
# 방법 3: 반복문 2개 돌리니까 10000 * 10000이라 시간 오버됨
# answer = []
# n = len(prices)
# # 가격이 떨어지지 않는 기간을 계속 기록해야 함
# # 가격이 떨어진 것도 떨어진 기간 유지 시간을 기록해야 하는 듯?! - 20분까지의 생각
# for i in range(n):
#     tmp = 0
#     for j in range(i + 1, n):
#         if prices[i] <= prices[j]:
#             tmp += 1
#     answer.append(tmp)

# 풀이참고
def solution(prices):
    n = len(prices)
    # 각 자리가 가질 수 있는 주식 가격이 떨어지지 않는 최대 시간의 배열 생성
    answer = [i for i in range(n - 1, -1, -1)]

    # 주식 가격이 떨어지는 경우 찾기
    stack = [0]
    for i in range(1, n):
        # stack이 존재하고, stack 가장 마지막 가격이 price 현재가보다 크다면
        # == 가격이 떨어진다면
        while stack and prices[stack[-1]] > prices[i]:
            # 스택의 가장 첫번째 값(인덱스)를 꺼내고
            # 해당 인덱스의 값 갱신 : 현재 prices인덱스 i - 스택 인덱스
            j = stack.pop()
            answer[j] = i - j  # index가 초 시점이라 index 차이를 넣는듯?
        # 순회하는 인덱스를 stack에 넣기
        stack.append(i)

    return answer