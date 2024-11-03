from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 도시 개수, 도로 개수
# 도로가 추가되는 것을 갱신하며 각 도로 1번부터 n번까지 1번에 가면서 거치는 도로 개수를 구해 출력한다
# 도로 상태를 가공해서 나타내야 함
# (1) 인접 행렬: 이차원배열로 각 도시별로 0, 1을 통해 연결된 도시들을 표현하는 것 => 불필요한 메모리 많아짐
# (2) 인접 리스트: 도시 별로 연결된 도시 번호를 바로 리스트에 넣어서 표현
# 도시들의 초기 연결 상태 - 인접리스트 형태
connected = dict()
for _ in range(m):
    a, b = map(int, input().split())
    # connected[a] = b - 이렇게만 쓰면 덮어씌워진다
    # 각 도시에 대해 연결 리스트 초기화 및 양방향 추가
    if a not in connected:
        connected[a] = []
    if b not in connected:
        connected[b] = []
    connected[a].append(b)
    connected[b].append(a)

def bfs():
    # 각 도시에 대한 거리 배열, n+1해서 도시 번호와 인덱스를 맞춤
    distances = [-1] * (n+1)
    # 1번 도시에서 출발해서 다른 모든 도시로 가는데 필요한 거리를 구한다
    queue = deque([1])
    distances[1] = 0 # 수도는 방문 도시 수가 0

    while queue:
        now = queue.popleft() # 현재 도시 번호
        # 연결상태 딕셔너리에서 now 번호를 key로 하는 values 리스트를 가져온다
        # 만약 now가 connected에 없으면 빈 리스트를 반환해 오류가 발생하지 않게 한다
        for next in connected.get(now, []):
            if distances[next] == -1: # 아직 방문하지 않은 도시라면
                distances[next] = distances[now] + 1 # 여기까지 오기 전 방문한 기존 도시 개수 + 방문한 도시 1개 추가하면서 방문하게 함 
                queue.append(next)

    return distances[1:] # 1번부터 n번까지 최소 방문 도시 수
# 정비 계획 별 결과 출력
q = int(input()) # 도로 수
for _ in range(q):
    # 정비되어 추가된 연결 사항을 갱신해준다
    c, d = map(int, input().split())
    if c not in connected:
        connected[c] = []
    if d not in connected:
        connected[d] = []
    connected[c].append(d)
    connected[d].append(c)

    # 이 다음 인접리스트를 탐색하며 각 도시별로 1로 가는데 필요한 최소 도시 개수 확인
    result = bfs()
    print(' '.join(map(str, result)))