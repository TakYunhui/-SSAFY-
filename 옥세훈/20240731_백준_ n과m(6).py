from itertools import combinations

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

result = list(combinations(ls, m))

for i in result:
    print(*i)