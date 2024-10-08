from collections import deque

def solution(x, y, n):
    answer = []
    count = 0
    tmp = deque()
    # 뒤에서 시작
    tmp.append([y, count])

    # queue가 존재하는 동안 반복
    while tmp:
        here = tmp.popleft()
        count = here[1] + 1
        # 만약 x값 y 값이 같으면
        if here[0] == x:
            answer = here
            break

        else:            
            if here[0] > x:
                if here[0] % 2 == 0:
                    tmp.append([here[0]//2, count])
                if here[0] % 3 == 0:
                    tmp.append([here[0]//3, count])
                tmp.append([here[0] - n, count])


        print(tmp)
    if not answer:
        return -1
    else:
        return answer[1]


x = 2
y = 5
n = 4

print(solution(x, y, n))