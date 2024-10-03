def solution(n, words):
    answer = []
    man_num = 1
    dic = dict()

    # 첫 번째, 이미 말한 단어인지
    # 두 번째, 제대로 끝말있기를 했는지

    temp = words[0][-1]
    dic[words[0]] = 1

    for i in range(1, len(words)):
        print(words[i])

        if i % n == 0:
            man_num = 1
        else:
            man_num += 1

        # 중복되지 않은 단어인지
        if words[i] not in dic:
            dic[words[i]] = 1
        else:
            return [man_num, (i // n) + 1]

        # 제대로 된 끝말잇기 인지 확인
        if temp != words[i][0]:
            return [man_num, (i // n) + 1]
        else:
            temp = words[i][-1]

    answer = [0, 0]
    return answer