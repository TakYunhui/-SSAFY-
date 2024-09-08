# 회의실 배정
# 회의실 사용 가능한 회의의 최대개수 찾기

# dp?
# 배열인덱스에 시작시간 넣어두고 역순으로 찾기?


# 틀림
N = int(input())
arr = []
ans = 1

for _ in range(N):
    start, end = map(int, input().split())
    arr.append((end, start))

# arr.sort(reverse=True)
arr.sort()
end_t = arr[0][0]

for i in range(N):
    if (end_t <= arr[i][1]):
        ans += 1
        end_t = arr[i][0]

# print(arr)
print(ans)


