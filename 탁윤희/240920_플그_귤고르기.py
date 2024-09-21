def solution(k, tangerine):
    answer = 0
    # 구해야 할 값: k개 넣을 때, 최소 종류 수
    # 귤 배열 안 종류 별 갯수를 dict형으로 정리한 다음, k개에 맞춰 넣으면 될 듯?
    tangerine_dict = dict()
    for t in tangerine:
        if t in tangerine_dict:
            tangerine_dict[t] += 1
        else:
            tangerine_dict[t] = 1
            # 종류 별 귤을 크기 순으로 정렬
    sorted_tangerines = sorted(tangerine_dict.items(), key=lambda x: x[1], reverse=True)

    for t in sorted_tangerines:
        k -= t[1]
        answer += 1
        if k <= 0:
            break

    return answer