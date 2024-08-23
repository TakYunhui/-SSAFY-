# 최소 힙

# 1. 배열에 자연수 x 넣기
# 2. 배열에서 가장 작은값 출력, 그 값을 배열에서 제거
# 시작은 빈 배열

# 구현해야하나? 일단 구현되어있는 모듈 사용
# 시간초과

import heapq

N = int(input())

# arr = [0]*(N+1)
arr = []

for _ in range(N):
    num = int(input())

    if (num==0):
        # pop
        if (len(arr)==0):
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        # push
        heapq.heappush(arr, num)