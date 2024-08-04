from itertools import combinations_with_replacement

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

result = combinations_with_replacement(ls, m)
result = sorted(list(set(result)))

for i in result:
    print(*i)