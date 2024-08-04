from itertools import combinations

n, m  = map(int, input().split())
ls = sorted(map(int, input().split()))

result = list(combinations(ls, m))
result = sorted(list(set(result)))
for i in result:
    print(*i)