# 실버 4 : 어두운 굴다리
# 가로등 모두 같은 정수, 최소한의 높이 구하기
# 높이 h 범위만큼 비춤 (ex: 1이라면 -1 0 1) => 총 3
n = int(input()) # 굴다리 길이 : 0~n까지
m = int(input()) # 가로등 개수
# m개의 가로등 설치할 수 있는 위치 x => 한 줄에 m개가 오므로 for문 안 써도 됨, split로 구분 됨
lights = list(map(int, input().split()))
# 가로등 길이를 1부터 설정하여 전체 범위를 덮을 수 있는지 늘려가기  -> 브루트포스: 비효율적
# 가로등 위치 기준으로 높이 범위 보기


# 가로등이 1개면 양끝쪽 중 먼 곳이 높이
if m == 1:
    height = max(lights[0], n-lights[0])
else:
    # 초기 높이 : 시작점과 첫 가로등의 거리
    height = lights[0]

    # 가로등 간 거리를 확인하며 최소 높이 계산
    for i in range(m):
        # 현재 i가 마지막 가로등이라면
        if i == (m - 1):
            # 마지막 가로등과 굴다리 끝 사이의 거리 저장
            tmp = n - lights[-1]
        else:
            # 중간 가로등은 현재 가로등과 다음 가로등 사이의 거리 저장
            a = lights[i+1] - lights[i]
            # 거리가 홀수라면
            if a % 2:
                # 홀수 거리의 중앙을 비추기 위해 +1
                tmp = a // 2 + 1
            else:
                tmp = a // 2
        # 현재 계산된 높이와 tmp 중 더 큰 값으로 업데이트
        height = max(height, tmp)

print(height)