# 21921 블로그


import sys

sys.stdin = open('input.txt')


N, X = map(int, input().split(' '))

# 1일부터 N일까지 중에
# 구간 중에 X일 동안 가장 많이 들어온 방문자 수 출력

# 리스트에서 X 번째까지 더한 합이 가장 큰 경우

visitors = list(map(int, input().split(' ')))

max_visitor = 0
max_visitor_count = 0

for i in range(N - X + 1):
    sum_visitors = 0
    for j in range(i, i + X):
        # print(j, '번째 항목', visitors[j])
        sum_visitors += visitors[j]
    
    # 방문자 수 합이 기존 합보다 많을때
    if sum_visitors > max_visitor:
        # 값 갱신
        max_visitor = sum_visitors
        # 카운트는 1로 고정 (더 많은 값이 나오면, 다시 1로 갱신해야 하므로)
        max_visitor_count = 1

    # max_visitor가 0이 아니고 최대 합이 같을 때
    elif max_visitor != 0 and sum_visitors == max_visitor:
        # 카운트 추가
        max_visitor_count += 1
    # print(i, '번째')
    # print('총 방문자 합',max_visitor)
    # print('방문자 카운트', max_visitor_count)


if max_visitor_count != 0:
    print(max_visitor)
    print(max_visitor_count)
else:
    print('SAD')