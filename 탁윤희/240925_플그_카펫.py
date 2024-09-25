def solution(brown, yellow):
    answer = []
    # 가로, 세로 : x, y
    # 카펫 전체 넓이: x * y == b + y
    # 노란색 영역: (x-2) * (y-2)
    # ㄴ 갈색 영역이 가로 세로 각각 2칸씩 더 있을 예정이기 때문
    space = brown + yellow
    # space 의 약수 찾기
    # ㄴ x >= y이므로 반복문에서 작은 수부터 넣어 찾으므로 y를 넣고 나머지 x를 구한다
    for y in range(1, int(space ** 0.5) + 1):
        if space % y == 0:
            x = space // y

            # x, y로 구한 값이 노란 영역 값이 나온다면
            if (x - 2) * (y - 2) == yellow:
                answer = [x, y]

    return answer