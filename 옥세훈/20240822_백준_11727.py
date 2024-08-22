
n = int(input())
rec = [0] * 1001
rec[1] = 1

if n >= 2:
    rec[2] = 3
    for i in range(3, n+1):
        rec[i] = (rec[i-2] * 2) + rec[i-1]

print(rec[n]%10007)

# 우선 규칙을 찾는다.
# 첫 번째와 두 번째를 정한다.
# 공식을 도출해서 점화식을 만든다. 