def solution(name):
    n = len(name)
    # 알파벳 변경하는 데 드는 조작 횟수
    answer = sum(min(ord(char) - ord('A'), ord('Z') - ord(char) + 1) for char in name)
    
    # 커서 이동 최적 경로 계산
    move = n - 1
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        move = min(move, i + n - next_i + min(i, n - next_i))
    
    return answer + move