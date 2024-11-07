# 0, 1부터 시작이고
# 마지막 두 수 더하면 되니까
# while & append 하고 마지막 두 수만 더하도록..?

def solution(n):
    fibo = [0, 1]
    now = 2
    while now <= n:
        tmp = fibo[-2] + fibo[-1]
        fibo.append(tmp)
        now += 1
    

    return fibo[-1] % 1234567

n = 5

print(solution(n))