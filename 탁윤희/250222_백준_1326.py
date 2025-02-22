# 실버2. 폴짝폴짝
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
bridges = list(map(int, input().split()))
a, b = map(int, input().split())
# 0-based index
a -= 1
b -= 1
# 시작 위치 a, 점프 횟수 cnt = 0
q = deque([[a, 0]])
visited = [-1] * n
visited[a] = 1
while q:
    now, cnt = q.popleft()
    if now == b:
        print(cnt)
        break
    # 배수만큼 합 이동 - now, now + bridges[now], now + bridges[now] * 2
    for next in range(now, n, bridges[now]):
        if visited[next] == -1:
            visited[next] = 1
            q.append([next, cnt + 1])
    # 차 이동 - now - bridges[now], now - bridges[now] * 2
    for next in range(now - bridges[now], -1, -bridges[now]):
        if visited[next] == -1:
            visited[next] = 1
            q.append([next, cnt + 1])


else:
    print(-1) # b에 방문하지 못 할 시, -1

