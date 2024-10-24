def solution(n, words):
    answer = [0,0]
    full_round = len(words) // n
    this_round = 1
    tmp = []
    for i in range(len(words)):
        if i != 0 and i % n == 0:
            this_round += 1
        # 첫번째, 끝말잇기가 안되는 경우.
        # 첫번째 단어라면 일단 임시 리스트에 넣기
        if not tmp:
            tmp.append(words[i])
        else:
            # 끝말잇기 성립이 되지 않으면
            if tmp[-1][-1] != words[i][0]:
                answer = [i % n + 1, this_round]
                return answer
            # 이미 있는 단어를 말한다면
            elif words[i] in tmp:
                answer = [i % n + 1, this_round]
                return answer
            # 성립이 된다면
            else:
                tmp.append(words[i])

     

    return answer


n = 2

words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n, words))