# 11501 주식

import sys

sys.stdin = open('input.txt')

tc = int(input())

for _ in range(tc):
    result = 0
    days = int(input())
    chart = list(map(int, input().split()))
    # print(chart)
    count = 0
    tmp = 0
    for i in range(days):
        # 다음날 하락장이면
        if i < days - 1: 
            if chart[i] > chart[i + 1]:
                # 주가 * 주식 수에서 그동안 사온 누적값 빼기 
                result += chart[i] * count - tmp
                # print('판매!')
                # print('수익', result)
                # 팔았으므로 누적값, 카운트 초기화
                count = 0
                tmp = 0
                # continue
            # 상승장이면
            elif chart[i] <= chart[i + 1]:
                # 주식 사기
                # print('매수!')
                count += 1
                tmp += chart[i]
                # print('현재 총액', tmp)
        # 마지막 날이면
        elif i == days - 1:
            # 상승장이면
            if chart[i] > chart[i - 1]:
                result += chart[i] * count - tmp


    print(result)