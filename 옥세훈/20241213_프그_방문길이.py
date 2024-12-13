def solution(dirs):
    dic = {"U": (1, 0), "D" : (-1, 0), "R" : (0, 1), "L" : (0,-1)}
    
    si, sj = 5, 5
    check = set()
    for i in dirs:
        x, y = dic[i]
        di, dj = si+x, sj+y
             
        if 0 <= di < 11 and 0 <= dj < 11:
            check.add((si, sj, di, dj))
            check.add((di, dj, si, sj))
            si, sj = di, dj
    
    return len(check) // 2