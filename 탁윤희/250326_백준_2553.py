# 실버2. 마지막 팩토리얼 수
n = int(input())
# n!의 0이 아닌 마지막 자리 수
# 팩토리얼 계산 후, 마지막 자리 수부터 확인
answer = 1
# 팩토리얼 계산
# n이 20000까지니 최대 곱셈 20000
for i in range(1, n+1):
    answer *= i
# 문자열로 변환 후, 자리수 확인
answer = str(answer)
for i in answer[::-1]: # 뒷자리부터 확인하기 위해 문자열 뒤집기
    if i != '0':
        print(i)
        break


