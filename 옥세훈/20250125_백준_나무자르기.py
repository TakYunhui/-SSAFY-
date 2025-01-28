import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

trees.sort()
# print(trees)

high = trees[(n-1)//2]
# 나머지 합들
left = 0
right = (n - 1)
remain = 0
while remain < m:
    mid = (left + right) // 2
    remain = 0
    for i in range(mid, n):
        remain += (trees[i] - high)
    #     print(trees[i], high)
    # print(remain, "remain")

    if remain < m:
        high -= 1
    elif remain > m:
        high += 1
    else:
        print(high)
        exit()

    # 탐색 범위 설정
    if trees[mid] < high:
        left = mid + 1
    elif trees[mid] > high:
        left = mid

print(high)

# 현재 문제는, while 안에 for문으로 시간초과가 발생함...








