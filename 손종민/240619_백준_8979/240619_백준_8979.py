# 8979 올림픽


import sys

sys.stdin = open('input.txt')

# N : 국가의 수, K : 등수를 알고싶은 국가
N, K = map(int, input().split(' '))

nations = []

for _ in range(N):
    nationInfo = list(map(int, input().split(' ')))
    nations.append(nationInfo)
# nations 리스트 추가 완료

nations.sort(key=lambda x=0 : (-x[1], -x[2], -x[3]))
# 금, 은, 동 많은 순으로 정렬

# 틀리게 처리한 부분
# index = -1
# for nation in nations:
#     index += 1
#     if nation[0] == K:
#         print(index)
#         break

# 등수 처리
rank = 1
results = {}        # 랭크를 담을 딕셔너리
results[nations[0][0]] = rank
for i in range(1, N):
    if nations[i][1:] == nations[i-1][1:]:
        results[nations[i][0]] = rank
    else:
        rank = i + 1            ## 공동 등수 처리
        results[nations[i][0]] = rank

print(results[K])