# 블로그
# 구간합? 누적합?
N, X = map(int, input().split())
visits = list(map(int, input().split()))
sum_list = [0] * (N+1)
max_num = -1
cnt = 0

for i in range(N):
    sum_list[i+1] = sum_list[i]+visits[i]
# print(sum_list)

for i in range(X, N+1):
    tmp = sum_list[i] - sum_list[i-X]
    if (max_num < tmp):
        cnt = 1
        max_num = tmp
    elif (max_num == tmp):
        cnt += 1

if (max_num == 0):
    print ("SAD")
else:
    print(max_num)
    print(cnt)