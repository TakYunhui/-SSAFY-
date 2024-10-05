def solution(want, number, discount):
    answer = 0
    # 할인 받는 순서 상관 없이 10일 안에 전체 want 내 요소들을 할인 받을 수 있는지 보면 됨
    # discount를 i번 부터 10개 동안 보면서 want 내 요소들 다 포함하는지 보면 될듯?
    # 하지만 항상 10개 배열을 다 만들어서 전체를 보는 건 비효율적이다
    # => 슬라이딩 윈도우로 상태를 1개씩 갱신
    # 1. 처음 10일간 초기 할인 상태 찾기
    # 2. 한 칸씩 이동하면서 빠진 제품을 빼고, 새로 들어오는 제품을 넣는다
    # 3. 수량이 want & number 조건에 맞는지 확인
    # 근데 list 보다 dict형태로 다 만들어서 비교하면 좋지 않나?
    want_dict = dict()
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    discount_dict = {}
    for i in range(10):
        product = discount[i]
        if product in discount_dict:
            discount_dict[product] += 1
        else:
            discount_dict[product] = 1

    def check_match():
        for key in want_dict:
            if discount_dict.get(key, 0) != want_dict[key]:
                return False
        return True

    # 첫 10일을 먼저 확인
    if check_match():
        answer += 1

    # 4. 슬라이딩 윈도우로 한 칸씩 이동하면서 확인
    for i in range(10, len(discount)):
        # i-10 번째 제품을 discount_dict에서 제거
        prev_product = discount[i - 10]
        if discount_dict[prev_product] == 1:
            del discount_dict[prev_product]
        else:
            discount_dict[prev_product] -= 1

        # 현재 i 번째 제품을 discount_dict에 추가
        new_product = discount[i]
        if new_product in discount_dict:
            discount_dict[new_product] += 1
        else:
            discount_dict[new_product] = 1

        # 업데이트된 discount_dict를 확인
        if check_match():
            answer += 1

    return answer