# 실버2. k보다 큰 구간
n = int(input())
numbers = list(map(int, input().split()))
k = int(input())
answer = 0
l, r = 0, 0 # 인덱스 모두 0에서 시작해서 조건 만족시 늘려가기
tmp = 0 # 구간합
while l <= r:
    # 구간합이 k보다 크면
    if tmp > k:
        # 이후 구간들의 구간합도 k보다 크니까 모두 추가
        answer += (n-r+1)
        # 왼쪽 인덱스 하나 이동시키기, 이동한 만큼 구간합 줄임
        tmp -= numbers[l]
        l += 1
    # 오른쪽 인덱스가 끝에 도달했으면 종료
    elif r == n:
        break
    # 구간합이 k보다 작으면(이하)
    else:
        # 구간합 늘리기, 오른쪽으로 이동한 만큼 구간합 증가
        tmp += numbers[r]
        r += 1
print(answer)