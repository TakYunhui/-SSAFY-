import sys

input = sys.stdin.readline

n, c = map(int, input().split())
arr = list(map(str, input().split()))
dic = dict()

for i in range(n):
    if arr[i] not in dic:
        dic[arr[i]] = 1
    else:
        dic[arr[i]] += 1

dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
# print(dic)

result = []
for i in dic:
    for j in range(i[1]):
        result.append(i[0])

print(*result)