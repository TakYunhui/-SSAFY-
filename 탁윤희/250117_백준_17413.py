# 실버3. 단어뒤집기 2
s = list(input())
stack = []

# 태그/단어 별로 구분해서 저장
tag = False
tagging_word = ""
word = ""

for i in s:
    if i == "<":  # 태그 시작
        if word:  # 태그 시작 전에 있던 단어 처리
            stack.append(word[::-1])
            word = ""
        tag = True
        tagging_word += i
    elif i == ">":  # 태그 끝
        tagging_word += i
        stack.append(tagging_word)
        tagging_word = ""
        tag = False
    elif tag:  # 태그 내부
        tagging_word += i
    elif i == " ":  # 공백 처리 (태그 외부)
        if word:  # 단어 처리
            stack.append(word[::-1])
            word = ""
        stack.append(" ")  # 공백 그대로 추가 (*내가 놓친 포인트! 공백을 아예 단어일 때 넣어주면 됐음)
    else:  # 단어 처리
        word += i

# 마지막 단어 처리
if word:
    stack.append(word[::-1])

# 리스트를 문자열로 결합하여 출력
print("".join(stack))