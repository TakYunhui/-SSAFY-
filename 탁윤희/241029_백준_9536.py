# 실버3. 여우는 어떻게 울까?
t = int(input())

for _ in range(t):
    sound = list(input().split())
    while True:
        sentence = input().split()
        n = len(sentence)
        # what does the fox say? 입력 시 종료
        if n == 5:
            break
        else:
            # 그 외의 경우는 다 n이 3개이므로 울음소리가 입력됨
            # 울음소리를 제거해준다
            # 하지만 리스트 내 remove만 하면 단독 1개만 제거된다
            # 내장 함수 filter를 이용한다(CPython 인터프리터)
            # for문은 조건을 만족할 때마다 배열을 재배치해야하므로 시간복잡도가 높다
            sound = list(filter(lambda x:x != sentence[2], sound))

    print(*sound)