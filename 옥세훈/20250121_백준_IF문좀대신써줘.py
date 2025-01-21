import sys

n, m = map(int, input().split())
named = [sys.stdin.readline().split() for _ in range(n)]
named.sort(key=lambda x : int(x[1]))
numbers = [int(sys.stdin.readline()) for _ in range(m)]

# print(named)
# print(numbers)

for number in numbers:
  right = len(named)
  left = 0
  res = 0

  while left <= right:
    mid = (left + right) // 2

    if int(named[mid][1]) < number:
        left = mid + 1
    else:
       res = mid
       right = mid - 1
  
  print(named[res][0])
