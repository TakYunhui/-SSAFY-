def solution(order):
    n = len(order)
    idx = 0
    num = 0
    
    st = []
    while idx < n:
        if order[idx] > num:
            num += 1
            st.append(num)
        elif order[idx] == st[-1]:
            st.pop()
            idx += 1
        else:
            return idx
    
    return idx