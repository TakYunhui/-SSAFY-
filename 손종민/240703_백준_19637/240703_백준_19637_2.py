# 19637 IF문 좀 대신 써줘
import sys

input = sys.stdin.read

# 이진 탐색 함수 만들기
def find_title(titles, power):
    # low, high 값 지정
    low, high = 0, len(titles) - 1
    # 탐색 기준
    while low < high:
        # 중간값 지정
        mid = (low + high) // 2
        # 입력값이 중간 값보다 같거나 작으면
        if power <= int(titles[mid][1]):
            # 최대값 중간값으로 갱신
            high = mid
        # 입력값이 중간값보다 크면
        else:
            # 최소값 중간값으로 갱신
            low = mid + 1
    # 다 찾으면 가장 낮은 title 출력
    return titles[low][0]

data = input().split()
N, M = int(data[0]), int(data[1])
titles = []

idx = 2
for _ in range(N):
    name = data[idx]
    power_limit = int(data[idx+1])
    titles.append((name, power_limit))
    idx += 2

for i in range(M):
    power = int(data[idx + i])
    print(find_title(titles, power))