import sys

# 입력이 많을 때 빠르게 입력받기 위한 설정
input = sys.stdin.readline

# n개의 칭호와 m명의 캐릭터 정보 받기
n, m = map(int, input().split())

# 칭호와 그에 해당하는 전투력을 입력받아 저장
titles = [input().split() for _ in range(n)]
# 전투력을 정수로 변환
for i in range(n):
    titles[i][1] = int(titles[i][1])

# 캐릭터들의 전투력 입력받기
characters = [int(input().strip()) for _ in range(m)]

# 이진 탐색을 위해 titles를 전투력 기준으로 오름차순 정렬
titles.sort(key=lambda x: x[1])

# 각 캐릭터의 전투력에 맞는 칭호를 출력
for char in characters:
    left, right = 0, n - 1
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if titles[mid][1] >= char:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    print(titles[result][0])