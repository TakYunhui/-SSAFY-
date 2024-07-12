# 리스트에 올라있는 점수 N
# 새로운 점수
# 최대 올라갈 수 있는 점수 개수 P


import sys

sys.stdin = open('input.txt')

N, newPoint, P = map(int, input().split())

# print(newPoint)

if N == 0:
    # 기존 점수가 없으면
    # 어떻게 해도 1등이므로
    print('1')
else:
    pointList = list(map(int, input().split()))
    # 점수 순회하면서
    result = 1
    count = 1
    for point in pointList:
        # 같거나 크면 등수 밀어야
        if point > newPoint:
            result += 1
            count += 1
        elif point == newPoint:
            count += 1
        # 새 점수보다 작으면
        else:
            # 멈추기
            break
    if count > P:
        print('-1')
    else:
        print(result)