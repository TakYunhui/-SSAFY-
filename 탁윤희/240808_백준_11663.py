# 실버 3. 선분 위의 점
import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline


def count_dot(start, end, dots):
    # 시작점 이상인 첫 번째 점의 위치
    left_idx = bisect_left(dots, start)
    # 끝 점 이하인 마지막 점의 다음 위치
    right_idx = bisect_right(dots, end)

    return right_idx - left_idx

n, m = map(int, input().split())
dots = sorted(list(map(int, input().split())))

for _ in range(m):
    start, end = map(int, input().split())
    print(count_dot(start, end, dots))