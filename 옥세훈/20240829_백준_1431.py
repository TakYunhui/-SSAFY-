from curses.ascii import isdigit
import sys
input = sys.stdin.readline

n = int(input())

arr = [input().rstrip()  for _ in range(n)]


ls = sorted(arr, key=lambda x: (len(x), sum(int(j) for j in x if isdigit(j)), x))

for i in ls:
    print(i)
