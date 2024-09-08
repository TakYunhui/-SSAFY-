import sys

# sys.stdin = open('input.txt')

data = sys.stdin.readline

N = int(data())

predictions = []
real_ranks = []

for i in range(N):
    predictions.append(int(data()))
    real_ranks.append(i + 1)

result = 0

# 순서대로 보면서
for predict in predictions:
    # 실제 등수 하나씩 대입하면서, 절댓값 계산
    tmp = N + 1
    idx = 0
    for rank in real_ranks:
        anger = abs(predict - rank)
        # 비교값보다 작으면
        if anger < tmp:
            # 비굣값 갱신
            tmp = anger

            idx = real_ranks.index(rank)
    result += tmp
    real_ranks.pop(idx)

print(result)