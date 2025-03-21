# 어두운 굴다리
N = int(input())
M = int(input())

x = list(map(int, input().split()))

max_len = 0
first_last = 0

for i in range(M):
    if (i==0):
        first_last = x[i]-0
    else:
        tmp = x[i]-x[i-1]
        if (max_len < tmp):
            max_len = tmp
    if (i==(M-1)):
        tmp = N - x[i]
        if (first_last < tmp):
            first_last = tmp

if (max_len%2==1):
    tmp = (max_len+1)//2
else:
    tmp = max_len//2

if (tmp > first_last):
    print(tmp)
else:
    print(first_last)

