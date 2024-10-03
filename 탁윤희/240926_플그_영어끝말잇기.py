def solution(n, words):
    answer = [0, 0]
    used_words = set()

    for i in range(len(words)):
        current_word = words[i]
        # 중복된 단어거나 단어를 잘못 말했다면 현재 참가자 번호와 참가자가 말한 차례 반환
        # 단어가 잘못일 때: i > 0 의 조건이 있어야 함, 아니면 시작부터 오류로 취급! !
        if current_word in used_words or( i > 0 and current_word[0] != words[i-1][-1]):
            current_person = (i % n) + 1 # index가 0부터 시작해서 +1 한다
            current_turn = (i // n) + 1
            return [current_person, current_turn]
        used_words.add(words[i])

    return answer