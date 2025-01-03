def solution(x, y, n):
    answer = 0
    check = set()
    check.add(x)
    
    while check:
        if y in check:
            return answer
        
        test = set()
        
        for i in check:
            
            if i + n <= y:
                test.add(i+n)
            
            if i * 2 <= y:
                test.add(i*2)
                
            if i * 3 <= y:
                test.add(i*3)
                
        check = test
        answer += 1
        
    
    return -1