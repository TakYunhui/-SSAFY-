n = int(input())
graph = [0]
result = [0]
# 선배들의 답 1-base index로 맞게 넣음
for i in range(1, n+1):
    graph.append(int(input()))

# dfs: 연결된 답 visit에 기록
def dfs(start):
    visit[start] = True
    if not visit[graph[start]]:
        dfs(graph[start])

# 1번 선배부터 n번까지 확인
for i in range(1, n+1):
    # visit를 선배 별로 초기화해 i번 선배가 연결된 선배들 탐색
    visit = [False] * (n+1)
    dfs(i)
    # True 개수 세서 선배별로 result 기록
    result.append(visit.count(True))
# True가 가장 많은 선배 번호 가져와 출력
print(result.index(max(result)))