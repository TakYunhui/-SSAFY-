from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 인접 리스트 만들기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# bfs로 리스트 관계 탐색, 1번과 가장 먼 거리를 갖는 것들 모으기
# 개 중 번호가 가장 작은 것 출력!
visited = [-1] * (n+1) # 각 번호 별 거리 저장할 것
q = deque([1])
visited[1] = 0

while q:
    cur = q.popleft()
    for i in graph[cur]:
        if visited[i] == -1:
            visited[i] = visited[cur] + 1
            q.append(i)

# min, max function으로 비교 말고 if로 해결하기
number, max_length, cnt = 0,0,0
for i in range(1, n+1):
    if max_length > visited[i]: continue # 최대 거리보다 작으면 넘어감
    elif max_length == visited[i]:
        cnt += 1
        continue # 여기 컨티뉴 넣는 이유?
    elif max_length < visited[i]: # 현재 방문 값의 거리가 최대라면
        # 아래와 같이 정의하면 최대 거리의 가장 작은 번호 한번만 들어간다
        # 왜냐면 < 조건이어서 같은 값들은 cnt 카운트만 하게 됨
        number = i
        max_length = visited[i]
        cnt = 1
        continue

print(number, max_length, cnt)
