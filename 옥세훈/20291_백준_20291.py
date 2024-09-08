import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = dict()
ls = []
for i in range(n):
    name, ext = input().rstrip().split(".")
    if ext not in dic:
        dic[ext] = 1
    else:
        dic[ext] += 1

for i in dic.items():
    a, b = i
    ls.append([a, b])

ls = sorted(ls, key=lambda x: x[0])
for i in ls:
    print(*i)