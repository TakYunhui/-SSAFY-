import heapq, sys
input = sys.stdin.readline

n = int(input())


hq = []
for _ in range(n):
    num = int(input())

    if not num:
        print(heapq.heappop(hq)[1] if hq else 0)
        continue

    heapq.heappush(hq, (abs(num), num))

