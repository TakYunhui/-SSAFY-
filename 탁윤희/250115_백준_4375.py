# 실버3. 1
# 1로만 이루어진 n의 배수: 1, 11, 111, 1111
# 1. 1부터 n의 배수인지 (% n) 연산을 통해 확인
# 2. ㄴ n의 배수가 아니면 10을 곱하고 1을 더함 (다음 1로만 이루어진 수를 만들기 위해)
# 3. n의 배수를 찾으면 반복문 종료 후 정답 출력
while True:
    try:
        n = int(input())
    # 종료 조건이 따로 주어지지 않아 try except 이용
    except:
        break
    num = 1
    cnt = 1
    while True:
        if num % n != 0:
            num = num * 10 + 1
            cnt += 1
        else:
            break
    print(cnt)