# 파도반 수열

arr = [0, 1, 1,1,2,2,3,4,5,7,9] + [0] * 100

# print(arr)

for i in range(11, 101):
    arr[i] = arr[i-3] + arr[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    print(arr[N])