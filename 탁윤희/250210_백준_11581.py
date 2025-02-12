# 실버1. 구호물자
import sys
input = sys.stdin.readline
INF = 100000

# 교차로의 수
n = int(input())
cycle = False
# 배열 초기화
cross = [[INF for _ in range(n)] for _ in range(n)]

# 입력: 1. i번째 교차로와 연결된 교차로 수 2. 연결된 교차로 번호
for i in range(n-1): # 0부터 n-1번까지 존재
    m = int(input()) #i번 교차로와 연결된 교차로의 수
    c = list(map(int, input().split())) #i번째에서 갈 수 있는 교차로의 번호
    for j in c:
        # 0-based idx라서 j-1에 넣는다
        cross[i][j-1] = 1

# 플로이드-워셜: 모든 정점에서 모든 정점으로 가는 최단 거리 구하기
# 거쳐가는 노드
for k in range(n):
    # 시작 노드
    for i in range(n):
        # 도착 노드
        for j in range(n):
            # cross[i][j]: 현재 i에서 j까지의 최단 거리
            # cross[i][k] + cross[k][j]: i에서 k를 거쳐 j까지 가는 경로의 거리
            # 조건이 성립하면, cross[i][j] 값을 더 작은 거리로 갱신합니다.
            if (cross[i][j] > cross[i][k] + cross[k][j]):
                cross[i][j] = cross[i][k] + cross[k][j]

for i in range(n):
    for j in range(n):
        # cross[0][j]: 1번 교차로에서 j번 교차로까지의 거리
        # 1번 교차로에서 j 교차로가 연결되어있다면 (== 거리가 양수로 존재 & not INF)
        if 0 < cross[0][j] < INF:
            # i 와 j 사이 양방향 연결 존재 확인
            # 연결 조건: i -> j 및 j -> i 경로가 함께 존재
            if (0 < cross[i][j] < INF and 0 < cross[j][i] < INF):
                # 양방향 연결이 있다면(두 노드가 서로를 향해 돌아올 수 있으므로) 사이클이 있다고 판단
                cycle = True
                break

if cycle == True:
    print ("CYCLE")
else:
    print("NO CYCLE")