# 22233 가희의 메모장
import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
M = int(data[1])

print(data)
memo = set(data[2:N+2])

print(memo)
index = N + 2
results = []
for _ in range(M):
    words = set(data[index].split(","))
    index += 1

    memo -= words
            
    results.append(len(memo))


# 결과 출력
sys.stdout.write("\n".join(map(str, results)) + "\n")