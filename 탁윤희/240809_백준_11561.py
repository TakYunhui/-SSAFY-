# 실버 3. 징검다리
import sys
input = sys.stdin.readline

def binary_search(n):
    left, right = 0, int((2 * n) ** 0.5) # 근의 공식 이용
    result = 1

    while left <= right:
        mid = (left + right) // 2
        # 수열의 합 계산
        if mid * (mid + 1) // 2 <= n:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    print(binary_search(n))