# 실버 2. 사탕 게임
# 1. 각 행/열마다 C, P, Z, Y 개수 기록
# 2. 위에서 최대 개수가 있는 행/열만 다시 인접하여 바꿀 값 있는지 확인
# 3. 있다면 최대값 + 1 해서 리턴하면 되지 않을까?
# ==> 기록 비효율적, 행/열을 확인할 때 인접한 값을 바로 교환하여 최대연속개수 확인 후, 다시 바꿔줌
# 참고: https://velog.io/@rhdmstj17/%EB%B0%B1%EC%A4%80-3085%EB%B2%88-%EC%82%AC%ED%83%95-%EA%B2%8C%EC%9E%84-python-%EB%B8%8C%EB%A3%A8%ED%8A%B8%ED%8F%AC%EC%8A%A4
import sys
input = sys.stdin.readline

n = int(input())
candy = list(list(input().strip()) for _ in range(n))

def checkMax():
    max_cnt = 1 # 사탕 1개가 최초의 최대 개수가 됨
    # n * n 행열 최대 연속 개수 확인할 것
    for i in range(n):
        cnt = 1
        # 가로 확인
        for j in range(1, n):
            # j는 1부터 n-1까지니 -1 해도 범위 안 임
            if candy[i][j] == candy[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)
        # 세로 확인
        for j in range(1, n):
            if candy[j][i] == candy[j-1][i]:
                cnt += 1
            else:
                cnt = 1
            max_cnt = max(max_cnt, cnt)

    return max_cnt

result = 1
for i in range(n):
    for j in range(n-1):
        # 오른쪽 바꾸기
        # j + 1 이 n보다 작아야 범위안
        if j + 1 < n and candy[i][j] != candy[i][j + 1]:
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
            result = max(result, checkMax())
            # 확인 후, 사탕 자리는 원상복귀
            candy[i][j], candy[i][j + 1] = candy[i][j + 1], candy[i][j]
        # 왼쪽 바꾸기
        if i + 1 < n and candy[i][j] != candy[i + 1][j]:
            candy[i][j], candy[i+ 1][j] = candy[i+ 1][j], candy[i][j]
            result = max(result, checkMax())
            candy[i][j], candy[i + 1][j] = candy[i + 1][j], candy[i][j]

print(result)