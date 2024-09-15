def solution(s):
    answer = []
    # " "를 통해 공백도 구별해서 list에 넣어준다
    s = s.split(" ")
    for word in s:
        # 첫 글자는 대문자, 나머지는 소문자
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        # 공백은 그냥 추가
        else:
            answer.append(word)
    return " ".join(answer)