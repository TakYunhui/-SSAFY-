from collections import deque

def solution(x, y, n):
    answer = 0
    tmp = deque()
    # 뒤에서 시작
    tmp.append([y, answer])

    # queue가 존재하는 동안 반복
    while tmp:
        here = tmp.popleft()
        answer = here[1]
        # 만약 x값 y 값이 같으면
        if here[0] == x:

            break

        else:            
            if here[0] > x:
                if here[0] % 2 == 0:
                    tmp.append([here[0]//2, answer + 1])
                if here[0] % 3 == 0:
                    tmp.append([here[0]//3, answer + 1])
                if here[0] - n > x:
                    tmp.append([here[0] - n, answer + 1])


        print(tmp)
    if answer < x:
        answer == -1

    return answer


x = 2
y = 5
n = 4

print(solution(x, y, n))