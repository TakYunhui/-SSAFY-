from itertools import combinations_with_replacement

n, m = map(int, input().split())
ls = sorted(map(int, input().split()))

result = list(combinations_with_replacement(ls, m))

for i in result:
    print(*i)