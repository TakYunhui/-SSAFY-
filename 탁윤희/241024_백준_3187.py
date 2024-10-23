# 실버 1. 양치기 꿍
# 각 울타리 영역 안에 늑대 vs 양 수를 비교
# 양이 늑대 수 초과하면 양만 산다, 나머지는 늑대가 산다
# .: 빈공간, #: 울타리, v: 늑대, k: 양
r, c = map(int, input().split())
# split()을 하면 공백 없는 문자열 입력이기에 그냥 그대로 다 들어온다
# 입력을 바로 list화해서 쪼갠다
farm = list(list(input()) for _ in range(r))
visited = list(list(0 for _ in range(c)) for _ in range(r))

def dfs(x, y):
    # 처음 들어온 좌표를 스택에 추가
    stack = [(x, y)]
    # visited 방문 처리하여 중복 탐색 방지
    visited[x][y] = 1
    # 해당 영역에서의 늑대와 양의 수를 셀 변수들
    wolf = 0
    sheep = 0
    # 현재 좌표 값의 양, 늑대 유무를 따진다
    if farm[x][y] == "v":
        wolf += 1
    elif farm[x][y] == "k":
        sheep += 1

    while stack:
        cx, cy = stack.pop()
        # 대각선을 제외한 상하좌우로 이동한다
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = cx + dx
            ny = cy + dy
            # 목장 범위 내이고 방문한 영역이 아니라면
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                # 또한 울타리가 아니라면
                if farm[nx][ny] != "#":
                    # 다음으로 이동할 좌표로 채택, 방문 처리
                    stack.append((nx, ny))
                    visited[nx][ny] = 1
                    # 그 뒤, 늑대와 양 유무에 따른 cnt 처리
                    # 왜 여기서 하냐면 while문 도는 동안 셀 필요가 있기 때문
                    if farm[nx][ny] == "v":
                        wolf += 1
                    elif farm[nx][ny] == "k":
                        sheep += 1


    return sheep, wolf


total_sheep = 0
total_wolves = 0
for i in range(r):
    for j in range(c):
        # 울타리가 아니고, 방문한 영역이 아니라면 dfs 탐색 시작
        if farm[i][j] != "#" and not visited[i][j]:
            sheep, wolf = dfs(i, j)
            # dfs 탐색을 마치면 영역 안의 양과 늑대 수 비교해서 cnt
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolves += wolf

print(total_sheep, total_wolves)

