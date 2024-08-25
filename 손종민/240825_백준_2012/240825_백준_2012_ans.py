import sys

# 입력 받기
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
predictions = [int(data[i]) for i in range(1, N + 1)]

# 예상 등수 정렬
predictions.sort()

# 불만도 계산
result = 0
for i in range(N):
    result += abs(predictions[i] - (i + 1))

print(result)