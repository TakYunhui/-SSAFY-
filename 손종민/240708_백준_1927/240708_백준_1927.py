import sys

input = sys.stdin.read

import heapq

data = input().split()
N = int(data[0])
heap = []

for i in range(1, N + 1):
    num = int(data[i])
    if num == 0:
        if len(heap) == 0:
            print('0')
        else :
            selected = heapq.heappop(heap)
            print(selected)
    else:
        heapq.heappush(heap, num)