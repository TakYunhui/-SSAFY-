import sys
t = int(sys.stdin.readline())

for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    a_ls = list(map(int, sys.stdin.readline().split()))
    b_ls = list(map(int, sys.stdin.readline().split()))

    a_ls.sort()
    b_ls.sort()

    answer = 0
    largest = max(b_ls)
    for j in range(a):
        target = a_ls[j]
        if target > largest:
            answer += b
            continue

        left = 0
        right = (b-1)
        res = 0

        while left <= right:
            mid = (left + right) // 2

            if target <= b_ls[mid]:
                right = mid - 1
                res = mid
            else:
                left = mid + 1

        answer += res

    print(answer)
