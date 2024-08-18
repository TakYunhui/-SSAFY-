# 프린터 큐
# 1. 가장 앞 문서의 중요도 확인
# 2. 나머지 중 더 중요한게 있으면 이 문서는 맨 뒤로
# 3. 아니라면 인쇄

# N이 100 이하니까 다 검사해도 될듯?

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    cnt = 0
    same_cnt = 0

    if (N == 1):
        print(1)
    else:
        '''
        # 규칙발견해보려고함
        for i in range(N):
            # 나보다 중요도 높은애가 몇갠지 확인해야함
            if (doc[i]>doc[M]):
                cnt += 1
            # 나랑 중요도 똑같은 애는 몇개인가
            elif (i!=M and doc[i]==doc[M]):
                same_cnt += 1

        if (same_cnt == 0):
            print(cnt+1)
        else:
            print('aa')
        '''
        imp = doc[M]
        doc[M] = 0

        # 전수조사
        while True:
            if (doc[0]!=0):
                if (doc[0] < imp):
                    first = doc.pop(0)
                    doc.append(first)
                else:
                    for i in range(N):
                        if doc[0] < doc[i]:
                            first = doc.pop(0)
                            doc.append(first)
                            break
                    else:
                        cnt += 1
                        doc.pop(0)
                        doc.append(-1)

            else: # 타겟 문서
                for i in range(N):
                    if imp < doc[i]:
                        first = doc.pop(0)
                        doc.append(first)
                        break
                else:
                    cnt += 1
                    break
        print(cnt)