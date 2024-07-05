# 1138 줄 세우기
# 인덱스로 접근하면 될 것 같은데...
# 정렬을 작은 순서부터? 큰 순서부터?
# 작은 사람부터 세우는 게 맞다
import sys

input = sys.stdin.read()

data = list(input)
N = data[0]
answers = data[1:N]

print(answers)

result = [0 for _ in range(N - 1)]

for i in range(1, N):
    