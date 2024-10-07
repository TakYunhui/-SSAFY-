def solution(n, left, right):
    answer = []
    # 제한 사항의 크기를 보면 단순 구현으로는 시간 효율 면에서 맞지 않다
    # 2차원 배열 만들 필요 X : 인덱스로 값 계산
    # k = (k//n, k%n) + 1 - 좌표 행/열 번호 중 더 큰 값에 1 을 더함
    for i in range(left, right+1):
        answer.append(max(i//n, i%n) + 1)
    return answer