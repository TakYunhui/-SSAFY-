import sys

n, c = map(int, input().split())
arr = [int(sys.stdin.readline()) for _ in range(n)]
arr.sort()

# 가장 인접한 두 거리 사이를 출력 1 2 4 8 9 => 1~4 == 3
# 기준 1 : 가장 인접한 거리 => target
# 기준 2 : c개를 다 사용
target = n // c # => 최소 거리
# 순서가 그럼 일단 최대한 떨어트려서 배치?
left, right = 0, n-1
res = 0
while res < c:

    while left <= right:
        mid = (left + right) // 2

        # c개를 분배하면서, 그 간격을 체킹하고, 이를 비교하며 값을 바꿔나가야하는디
        if arr[mid] < target and res < c:
            pass


# 7 3
# 2...1
# 1, 2, 3, 4, 5, 6, 7
# 3

# 인덱스랑, 차를 햇갈리면 안될듯?