# 골드 5. 회장뽑기
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
# 인접 리스트 : [[], [2], [1, 3, 4], [2, 4, 5], [3, 5, 2], [4, 3]]
graph = [[] for _ in range(n+1) ]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

# (겹)친구가 많을 수록 - 연결된 수가 많을 수록 회장 후보
# 각 회원 별로 bfs 탐색해서 연결된 점수 계산
'''
모두와 친구: 1점
친구/친구의 친구: 2점
친구/친구의 친구/친구의 친구의 친구: 3점...
건너다리가 많아질 수록 점수 증가 
=> 가장 작은 점수가 회장 후보 
--> 다른 회원들까지의 최단 거리 중 최대값을 점수로 취급! 
'''
def bfs(number):
    visited = [-1] * (n+1) # 방문 배열
    q = deque([number])
    visited[number] = 0

    while q:
        current = q.popleft()
        for i in graph[current]:
            if visited[i] == -1:
                visited[i] = visited[current] + 1
                q.append(i)
    return max(visited[1:])

# bfs 로 구한 각 점수를 scores 배열에 넣고 최소 점수 구하기
scores = []
for i in range(1, n+1):
    scores.append(bfs(i))
score = min(scores)

candidates = []
for i in range(1, n+1):
    if scores[i-1] == score:
        candidates.append(i)
print(score, len(candidates))
print(*candidates)