# 실버1. 싫은데요
n, m = map(int, input().split()) # 구멍 개수 n, 최대 부피 m
holes = list(map(int, input().split())) # 구멍들

# 연속된 구멍들로 최대 m까지 늘릴 수 있음 => 데이터 정렬 불가
# 가능한 많은 부피의 구멍들

if n == 1:
    if holes[0] > m:
        print(0)
    else:
        print(holes[0])
else:
    # 두 포인터
    answer = 0
    l, r = 0, 1
    tmp = holes[0]
    # 오른쪽 인덱스가 n(끝)에 도달하면 종료
    while r < n:
        # 최대 부피 m보다 구간합이 낮으면 오른쪽 인덱스 증가시킴
        if tmp + holes[r] <= m:
            tmp += holes[r]
            r += 1
            answer = max(answer, tmp)
        else:
            tmp -= holes[l]
            l += 1

    print(answer)
