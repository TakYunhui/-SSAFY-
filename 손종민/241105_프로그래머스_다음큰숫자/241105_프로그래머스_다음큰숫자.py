from collections import Counter

def solution(n):
    bin_n = Counter(bin(n))['1']
    next_num = n + 1
    while n:
        if Counter(bin(next_num))['1'] == bin_n:
            return next_num
        else:
            next_num += 1
    

n = 78
print(solution(n))