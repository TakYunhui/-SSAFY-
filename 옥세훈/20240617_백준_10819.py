from itertools import permutations
n = int(input())

ls = list(map(int, input().split()))
perm = list(permutations(ls, n))
for i in perm:
    print(i)


total_ls = []
for i in perm:
    total = 0
    for j in range(n-1):
        total += abs(i[j] - i[j+1])
    total_ls.append(total)

print(max(total_ls))