# 실버3. 후위 표기식 2 - 런타임에러 (EOFerror?)
# 입력 받는 값이 없을 때 에러
# 후위 계산 : https://siyoon210.tistory.com/2
# 소수점 출력 : https://velog.io/@cod2048/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%86%8C%EC%88%98%EC%A0%90-%EC%B6%9C%EB%A0%A5-%EC%9E%90%EB%A6%AC%EC%88%98-%EC%A7%80%EC%A0%95
n = int(input())
cal = '*+/-'
q = list(input())
stack = []
result = []
for i in range(len(q)):
    if q[i] not in cal:
        # 이 쪽에서 에러가 난듯??? 왜냐면 2번 예제 생각하면 A=1 하나로 대입되는데
        # 내 코드는 A 나올 때마다 숫자 새로 받아야 하기 때문
        stack.append(int(input()))
    else:
        # 먼저 뽑은 쪽이 뒤에 있는 숫자
        num2 = stack.pop()
        num1 = stack.pop()
        if q[i] == "+":
            stack.append(num1 + num2)
        elif q[i] == "-":
            stack.append(num1 - num2)
        elif q[i] == "*":
            stack.append(num1 * num2)
        elif q[i] == "/":
            stack.append(num1 / num2)

print(f'{stack[0]:.2f}')