# 실버3. 놀라운 문자열
# 문자열 짝지은 게 다 다르면 surprising
# 하나라도 같은 게 나오면 not surprising
while True:
    word = input()
    n = len(word)
    if word == "*":
        break
    # 문자열 짝짓기 -> 이중 반복문
    check = True
    for i in range(1, n):
        lst = []
        # D-쌍 확인 : lst에 D-쌍 글자 넣기
        for j in range(n-i):
            lst.append(word[j]+word[j+i])
        # 중복되는 쌍 확인 : lst[k]가 k+1부터 다음 배열까지 안에 있는지 확인
        for k in range(len(lst)):
            if lst[k] in lst[k+1:]:
                check = False
    if check:
        print(f"{word} is surprising.")
    else:
        print(f'{word} is NOT surprising.')
