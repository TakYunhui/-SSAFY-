A, B = map(str, input().split())

Alen = len(A)
Blen = len(B)
cnt = 0

# 길이가 같은 경우
if Alen == Blen:
    for i in range(Alen):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)
# 길이가 다른 경우
else:
    # A가 B안에 있는 경우
    if A in B:
        print(0)
    else:
        front, back = 0, 0
        for i in range(Alen//2):
            if A[i] != B[i]:
                front += 1
            if A[Alen-i-1] != B[Blen-i-1]:
                back += 1

        num = Blen - Alen
        print(front, back)
        if front > back:
            A = B[:num] + A
        elif front < back:
            A = A + B[-num:]
        else:
            # 여기가 문제임 -> 뭔가 다른 방식으로 풀어야 할듯, stack 이라던가
            A = B[:num] + A + B[-num:]
            print(A)

        for i in range(Blen):
            if A[i] != B[i]:
                cnt += 1

        print(cnt)


# abc xxbzzz
# 2
