from itertools import product

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

result = list(product(ls, repeat=m))

for i in result:
    print(*i)