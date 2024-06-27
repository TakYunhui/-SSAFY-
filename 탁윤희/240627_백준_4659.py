# 실버 5 : 비밀번호 발음하기
while True:
    try:
        p = list(input())
        if ''.join(p) == "end":
            break
        check1 = 0
        check2 = 1
        check3 = 1

        # 1번 조건 : 모음 포함 확인
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in vowel:
            if i in p:
                check1 = 1
                pass

        c_cnt = 0
        v_cnt = 0
        # 2번 조건 : 모음 또는 자음이 3개 연속으로 오는지 확인
        for i in p:
            if i in vowel:
                v_cnt += 1
                c_cnt = 0
            else:
                v_cnt = 0
                c_cnt += 1

            if v_cnt == 3:
                check2 = 0
                pass
            elif c_cnt == 3:
                check2 = 0
                pass


        # 3번 조건 : 같은 글자 연속 확인 - e나 o만 허용
        for j in range(1, len(p)):
            if p[j-1] == p[j]:
                if p[j] != "e" or p[j] != 'e':
                    check3 = 0
                    pass


        if check1 and check2 and check3:
            print(f"<{''.join(p)}> is acceptable.")
        else:
            print(f"<{''.join(p)}> is not acceptable.")
    except EOFError:
        break