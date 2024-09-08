t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    arr = sorted(arr)
    # 한마디로, 인접한(마지막과 첫번째 포함) 통나무의 차의 최댓값이 제일 작게 해라.

    small_num = 0
    for j in range(2, n):
        small_num = max(small_num, abs(arr[j] - arr[j-2]))
    print(small_num)