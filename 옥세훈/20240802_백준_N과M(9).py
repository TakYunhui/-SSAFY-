from itertools import permutations

n, m  = map(int, input().split())
ls = (map(int, input().split()))

result = list(permutations(ls, m))
result = sorted(list(set(result)))
for i in result:
    print(*i)