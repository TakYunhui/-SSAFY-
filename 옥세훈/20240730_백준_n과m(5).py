from itertools import permutations

n, m = map(int, input().split())
ls = list(map(int, input().split()))


check = list(permutations(ls, m))
check.sort()


for i in check:
    print(*i)

