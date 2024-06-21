#7568
## 나열하기

import sys

sys.stdin = open('input.txt')

# 사람 수 N
N = int(input())
personList = []

for _ in range(N):
    personInfo = list(map(int, input().split(' ')))
    personList.append(personInfo)

# 리스트에 넣었으니
# 나열하며 순위 계산

rankList = []
for i in range(N):
    # 다른 항목들과 비교?
    rank = 1

    for j in range(N):
        # 자신과는 비교할 필요 없으므로
        if i == j:
            pass
        if personList[i][0] < personList[j][0] and personList[i][1] < personList[j][1]:
            rank += 1

    rankList.append(rank)

print(*rankList, sep=' ')