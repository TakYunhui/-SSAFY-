from collections import deque

def solution(prices):
    answer = []
    # 좌측부터 빼야하므로 큐로 처리하기
    prices = deque(prices)
    # prices 안에 값이 있는 동안 while문 돌리기
    while prices:
        # 오래된 것 뽑기
        this_price = prices.popleft()
        minute = 0

        # 마지막 요소가 아니면
        if prices:
            # prices for문 돌면서 가격이 낮은지 세어주기
            for price in prices:
                minute += 1
                # 가격이 더 낮은 것 발견시 정지
                if price < this_price:
                    break
            answer.append(minute)
        else:
            answer.append(minute)


    return answer


prices = [1, 2, 3, 2, 3]

print(solution(prices))