# 수열

# 연속해서 커지거나, 연속해서 작아지는 수열(등호 포함) 중 가장 길이가 긴 것
# 길이 출력

# 이것도 어제처럼 dp+브루트포스?
# 근데 이건 브루트포스하기엔 N이 너무 크다
# 연속이니까 슬라이딩윈도우?

# 1 <= N <= 100_100

N = int(input())
arr = list(map(int, input().split()))

'''
# 내 아이디어
# 투포인터
# 이렇게 하니까 입력 2부터 자꾸 +1이 된 답이 나옴.
# 전부 같을때 못풀걸
is_ascend = True
is_equal = False
if (arr[0] == arr[1]):
    is_equal = True
elif (arr[0] > arr[1]):
    is_ascend = False
start = 0
end = 0
maxi = 1


# 만약 첫번째, 두번째가 크기가 같다면? 어떻게 하지?

for i in range(N-1):
    tmp = 1
    # 뒤에꺼랑 비교해서 뭐가 더 큰지 비교하기
    if (is_equal):
        if (arr[i] == arr[i+1]):
            tmp += 1
            end = i+1
    if (is_ascend): # 증가하는 수열
        if (arr[i] <= arr[i+1]):
            tmp += 1
            end = i+1
        else:
            is_ascend = False
            length = end - start + 1
            start, end = i, i+1
            if (maxi < length):
                maxi = length
    else: # 감소하는 수열
        if (arr[i] >= arr[i+1]):
            tmp += 1
            end = i+1
        else:
            is_ascend = False
            length = end - start + 1
            start, end = i, i+1
            if (maxi < length):
                maxi = length

print(maxi)
'''

# dp로 풀기
ascd = [1] * N # 증가수열
desc = [1] * N # 감소수열

for i in range(1, N):
    if arr[i-1] <= arr[i]:
        ascd[i] = ascd[i-1] + 1

for i in range(1, N):
    if arr[i-1] >= arr[i]:
        desc[i] = desc[i-1] + 1

max1 = max(ascd)
max2 = max(desc)

print(max(max1, max2))