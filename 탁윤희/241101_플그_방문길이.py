# 1차 시도: 단순 구현, 배열 범위가 맞으면 +1 해준다
# 5/100 점
# def solution(dirs):
#     answer = 0
#     # 좌표 평면 & 캐릭터 초기 위치 설정
#     arr = list([0] * 10 for _ in range(10))
#     fx, fy = 4, 4
#     arr[fx][fy] = 1
#
#     for dir in dirs:
#         if dir == "U":
#             nx, ny = fx + 1, fy
#         elif dir == "D":
#             nx, ny = fx - 1, fy
#         elif dir == "L":
#             nx, ny = fx, fy - 1
#         elif dir == "R":
#             nx, ny = fx, fy + 1
#
#         if 0 <= nx < 9 and 0 <= ny < 9:
#             arr[nx][ny] = 1
#             fx, fy = nx, ny
#
#     for x in arr:
#         answer += x.count(1)
#
#     return answer


# set으로 이동 방향 관리
def solution(dirs):
    loc = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    answer = set()
    x, y = 0, 0
    for d in dirs:
        dx, dy = loc[d]
        nx, ny = x + dx, y + dy
        # 절댓값으로 범위 안인지 확인
        if abs(nx) <= 5 and abs(ny) <= 5:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x = nx
            y = ny

    return len(answer) // 2