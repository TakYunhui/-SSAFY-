# 실버3. 늑대와 양
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
# split()을 넣으면 한 줄이 리스트 한 요소로 들어가니 그냥 input()한 걸 list()화해서 문자를 나눔
graph = list(list(input()) for _ in range(R))
# 상하좌우direction
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]
# 늑대가 양에게 갈 수 있으면 True, 없으면 default False
boolean = False

# 늑대의 상하좌우에 양이 있는지 확인 > 있으면 boolean True
for i in range(R):
    for j in range(C):
        # 늑대 위치를 찾아서 늑대가 양에 닿을 수 있는지 확인하는게 직관적
        if graph[i][j] == "W":
            for k in d:
                x = i + k[0]
                y = j + k[1]
                # 다음 위치 x, y가 리스트 범위를 벗어나면 넘김
                if x <= -1 or x >= R or y <= -1 or y >= C:
                    continue

                if graph[x][y] == "S":
                    boolean = True
                    break

if boolean:
    print(0)
else:
    print(1)
    # 늑대/양 위치 제외하고 모두 울타리 설치
    # 왜냐? 울타리 최소 개수 구하는 게 아니라 그냥 다 울타리 쳐두면 됨
    for i in range(R):
        for j in range(C):
            if graph[i][j] == ".":
                graph[i][j] = "D"

    for k in graph:
        print(''.join(k))