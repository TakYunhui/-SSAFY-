def solution(n, t, m, p):
    answer = "0"
    check = "0123456789ABCDEF"
    
    for num in range(1, m*t):
        checking = ""
        
        while num > 0:
            num, y = divmod(num, n)
            checking += check[y]
        
        answer += checking[::-1]
    
    return answer[p-1::m][:t]



