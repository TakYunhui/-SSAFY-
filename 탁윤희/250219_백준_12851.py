# 골드4. 숨바꼭질 2(복습)
from collections import deque

n, k = map(int, input().split())
# 방문 check, 처음 위치 n의 time을 0으로 두기 위해 -1로 배열 선언
visited = [-1] * (100001)
visited[n] = 0
q = deque([n]) # 현재 위치
cnt = 0 # 방법 수 count

# bfs 최단 거리만 구할 것
while q:
    now = q.popleft()

    if now == k: # 현재 위치가 k가 되면 방법 +1,
        cnt += 1
        continue # break를 쓰면 1개 구하고 끝나버리니 continue로 이어준다

    for next in now-1, now+1, now*2: # 걷기(+1, -1)와 순간이동(*2)
        if 0 <= next < 100001: # visited 배열 안에서 이동하게 범위 설정
            if visited[next] == -1:
                visited[next] = visited[now] + 1 # 시간 1초 늘리기
                q.append(next)
            elif visited[next] == visited[now] + 1: # 만약 이미 방문했고, 동일한 최단 거리로 저장되어 있다면
                q.append(next) # nx만 추가하여 방법의 수를 갱신할 수 있게 함

print(visited[k])
print(cnt)
