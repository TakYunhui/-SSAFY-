# 실버3. 거북이
# 명령 방향대로 이동시키고 이동하며 얻는 좌표를 저장하기?
# 그 뒤 x, y 최대-최소로 얻어지는 영역 넓이 구하기
# F: 앞으로 1칸 이동
# B: 뒤로 1칸 이동
# L: 왼쪽 90도 회전  - NWSE
# R: 오른쪽 90도 회전 - NESW
# ㄴ 항상 북쪽 기준으로 시작하니 위처럼 회전
t = int(input())
# 북동남서 0123

for _ in range(t):
    order = list(input())
    memory = set()
    x, y, d = 0, 0, 0
    for i in order:
        if i == 'F': # 앞으로 이동
            if d == 0: # 북쪽
                y += 1
            elif d == 1: # 동쪽
                x += 1
            elif d == 2: # 남쪽
                y -= 1
            else:        # 서쪽
                x -= 1
        elif i == 'B':  # 뒤로 이동
            if d == 0:  # 북쪽
                y -= 1
            elif d == 1:  # 동쪽
                x -= 1
            elif d == 2:  # 남쪽
                y += 1
            else:  # 서쪽
                x += 1

        elif i == 'L':  # 왼쪽으로 회전
            if d == 0:  # 북쪽에서 서쪽으로
                d = 3
            else:  # 그 외의 경우 방향 감소
                d -= 1

        elif i == 'R':  # 오른쪽으로 회전
            d += 1
            d %= 4  # 0~3의 범위를 유지 (순환)

        memory.add((x, y))  # 현재 좌표를 방문한 좌표에 추가

    # 방문한 좌표 중 최대 및 최소 x, y 값 초기화
    max_x, min_x = 0, 0
    max_y, min_y = 0, 0

    # 방문한 모든 좌표를 순회하면서 최대 및 최소 좌표 계산
    for x, y in memory:
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)

    # 직사각형의 높이와 너비 계산
    height = abs(max_y) + abs(min_y)
    width = abs(max_x) + abs(min_x)

    # 직사각형의 넓이를 출력
    print(height * width)