# 실버 2. 최대 곱
# 합이 s인 k 개의 양수
s, k = map(int, input().split())
li = [s//k for _ in range(k)]
for i in range(s%k):
    li[i] += 1
res = 1
for n in li:
    res *= n
print(res)
