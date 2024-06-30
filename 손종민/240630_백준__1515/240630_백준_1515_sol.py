import sys

sys.stdin = open('input.txt')

N = input()

result = 0


while True:
    # 최솟값은 1씩 올려가면서 비교
    result += 1
    num = str(result)
    print('현재 최솟값' , result)
    # N이 남아있는 동안 계속해서 반복
    while len(num) > 0 and len(N) > 0:
        # 현재 최솟값과 비교할 숫자의 맨 앞 자리가 같다면
        if num[0] == N[0]:
            # 앞에서 한 자리씩 지워주기
            N = N[1:]
        # 최솟값 갱신해주기
        num = num[1:]
        print('남은 숫자', N)
        print('비교 숫자', num)

    if N == '':
        print(result)
        break