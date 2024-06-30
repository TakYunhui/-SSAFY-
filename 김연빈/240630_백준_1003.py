# 피보나치 함수

# 다음 함수에서 0과 1이 몇번 출력되는지 구하라
'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
'''

'''
f(0) => 1, 0
f(1) => 0, 1
f(2) = f(1) + f(0) => 1, 1
f(3) = f(2) + f(1) => 1, 2
f(4) = f(3) + f(2) => 2, 3
f(5) = f(4) + f(3) => 3, 5
'''
T = int(input())

fibo = [[0, 0] for _ in range(42)]

fibo[0] = [1, 0]
fibo[1] = [0, 1]

for i in range(2, 41):
    fibo[i][0] = fibo[i-1][0] + fibo[i-2][0]
    fibo[i][1] = fibo[i-1][1] + fibo[i-2][1]

# print(fibo)

for _ in range(T):
    n = int(input()) # 0 <= n <= 40
    print(fibo[n][0], fibo[n][1])