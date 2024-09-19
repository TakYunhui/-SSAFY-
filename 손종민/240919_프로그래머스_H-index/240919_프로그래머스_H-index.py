def solution(citations):
    citations.sort()
    # print(citations)
    h = 1
    while h <= 1000:
        count = 0
        for citation in citations:
            if citation >= h:
                count += 1
        if count <= h:
            break
    return h


citations = [3, 0, 6, 1, 5]
print(solution(citations))