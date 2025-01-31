# 실버1. 수들의 합 6
# 가장 윗줄 숫자 경우의 수: 1부터 n까지 숫자의 순열
from itertools import permutations
from math import comb

def solve_pascal_triangle(n, f):
    # 조합 계수 미리 계산
    coefficients = [comb(n - 1, i) for i in range(n)]

    # 1부터 N까지 순열을 생성하여 검사
    # 순열 숫자를 사전순으로 생성하기에 가장 먼저 나온 걸 출력하면 사전순 출력이 됨
    for perm in permutations(range(1, n + 1)):
        # 각 자리 숫자와 해당 자리 조합 계수를 곱한 값의 총합
        total = sum(x * c for x, c in zip(perm, coefficients))
        # 총합이 f라면 정답
        if total == f:
            print(*perm)
            return

# 입력 처리
n, f = map(int, input().split())
solve_pascal_triangle(n, f)