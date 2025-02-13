# 실버1. 1, 2, 3 더하기 2
# n을 1, 2, 3의 사전순 합으로 나타내는 방법 중 k번째 식 구하기
n, k = map(int, input().split())
count = 0 # k번 카운트
answer = None # 정답
def backtrack(x, path): # x: 현재까지 합, path: 현재까지 숫자 리스트
    global count, answer
    if x == n: # 합이 n 이 되면
        count += 1 # cnt += 1
        if count == k: # k번째가 되면 answer 선언
            answer = '+'.join(map(str, path))
        return

    # 1 -> 2 -> 3 순으로 채워넣는다
    # 이때, 1로 채우는 값이 n에 도달하여야 첫번째 dfs 탐색 종료되고
    # 그 다음부터 1+2...식으로 탐색이 진행되는 개념
    for i in [1, 2, 3]:
        if x + i <= n:
            backtrack(x + i, path + [i])

# 시작: 0, []
backtrack(0, [])
print(answer if answer else -1)


