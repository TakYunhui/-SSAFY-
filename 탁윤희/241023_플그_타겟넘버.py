# 프로그래머스 레벨 2
def solution(numbers, target):
    global answer # 전역 변수 선언으로 함수에서 사용할 수 있게 함
    answer = 0
    # 현재 숫자의 인덱스, 현재까지 숫자합
    def dfs(idx, total):
        # 전역 변수 answer 쓴다고 다시 선언
        # 이거 안 하면 answer가 함수에서만 쓰이는 지역 변수로 인식됨
        # => Unbounded local variable Error 발생
        global answer
        # 현재 인덱스가 배열의 길이라면 숫자를 다 본 것이므로 종료
        if idx == len(numbers):
            # 현재 숫자합이 타겟과 같다면 answer +1
            if total == target:
                answer += 1
        # 다음 인덱스로 넘어가고
        # 현재 총합에 현재 숫자를 더하거나 뺀다
        dfs(idx + 1, total + numbers[idx])
        dfs(idx + 1, total - numbers[idx])
        return # 함수 종료

    dfs(0, 0) # idx: 0, total: 0으로 시작

    return answer