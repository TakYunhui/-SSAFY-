import sys
sys.stdin = open('input.txt')

# 입력 받기
N, X = map(int, input().split())
visitors = list(map(int, input().split()))

# 초기값 설정
current_sum = sum(visitors[:X])
max_sum = current_sum
max_count = 1

# 슬라이딩 윈도우를 사용하여 최대 방문자 수 찾기
for i in range(X, N):
    current_sum = current_sum + visitors[i] - visitors[i - X]
    if current_sum > max_sum:
        max_sum = current_sum
        max_count = 1
    elif current_sum == max_sum:
        max_count += 1

# 결과 출력
if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_count)