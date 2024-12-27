import math
from collections import deque

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False

    return True

def solution(n, k):
    answer = 0
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
        
    base = deque(base[::-1])
    q = deque()
    while base:
        # 순회하면서 수를 저장하고
        # 0을 만나면 죄다 pop
        # 만약 1밖에 없으면 제껴
        # 그리고 그 모인 수를 소수 판별
        
        num = base.popleft()
        if num != "0":
            q.append(num)
        else:
            check = ''
            while q:
                check += q.popleft()
        
            if check != "1" and check and is_prime(int(check)):
                answer += 1

    
    if len(q) > 0:
        last = int(''.join(q))
        if is_prime(last) and last != 1:
            answer += 1
    return answer