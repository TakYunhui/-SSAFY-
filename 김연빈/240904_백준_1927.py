# 최소 힙

# 240819 코드에 import sys만 추가

import sys
import heapq

input = sys.stdin.readline

N = int(input())

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