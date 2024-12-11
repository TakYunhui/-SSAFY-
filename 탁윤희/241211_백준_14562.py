from collections import deque

def bfs(S, T):
    q = deque()
    # 태균의 현재 점수, 라이벌 점수, 발차기 횟수를 큐로 관리
    q.append((S, T, 0))
    # bfs 탐색되었는지를 check하는 배열
    check = [-1]*(200)
    while q:
        node, t, c = q.popleft()
        # 아직 node가 라이벌 점수 이하이고 탐색하지 않은 node라면 탐색
        if node <= t and check[node] == -1:
            q.append((node*2, t+3, c+1))
            q.append((node+1, t, c+1))
            if node == t:
                return c

C = int(input())
for _ in range(C):
    S, T = map(int, input().split())
    print(bfs(S, T))