import sys
sys.stdin = open('input.txt')
from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split(' '))
    count = 0
    if N > 1:
        # 우선순위 판별을 위한 큐
        ls = list(map(int, input().split(' ')))
        que = deque(ls)

        # 문서의 출력 순서를 알기 위한 큐
        docs = []
        for i in range(N):
            docs.append(i)
        finder = docs[M]
        docs_que = deque(docs)
        
        # 일단은 큐 순회
        while que:
            highest = max(que)
            # 일단 두 큐에서 다 뽑기
            this_doc = que.popleft()
            this_doc_label = docs_que.popleft()
            # 남은 큐가 있고 우선순위가 높은 값이 아니면
            if this_doc != highest:
                # 순환시키기
                que.append(this_doc)
                docs_que.append(this_doc_label)
            # 남은 큐가 있고 우선순위가 제일 높은 값이면
            else:
                # 프린트 카운트 추가
                count += 1
                # 내가 찾던 값이면 멈추기
                if this_doc_label == finder:
                    break

    else:
        ls = [int(input())]
        count = 1
        
    
    print(count)