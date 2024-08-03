from itertools import product

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

result = product(ls, repeat=m)
result = sorted(list(set(result)))

for i in result:
    print(*i)