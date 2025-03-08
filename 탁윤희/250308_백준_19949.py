# 실버2. 영재의 시험
def back(n):
    global cnt
    # 정답 10개 선택
    if n == 10:
        s = 0
        # 답이 맞는지 ans 리스트와 비교해 점수 확인
        for j in range(10):
            if li[j] == ans[j]:
                s += 1
        if s >= 5: # 5점이상이면 cnt 추가
            cnt += 1
        return

    for i in range(1, 6): # 1번부터 5번까지 중에서 찍기
        # 현재 찍은 개수가 2개 이상, 현재 선택한 답이 그 전의 2개 답과 같으면
        if n > 1 and li[n-2] == li[n-1] == i:
            continue # 조건이 성립하지 않으니 넘김
        # 위 조건이 아니라면 현재 선택한 값을 답지에 추가
        li.append(i)
        # 백트래킹 진행 - 넣었다 뺀다
        back(n+1)
        li.pop()



li, cnt = [], 0
ans = list(map(int, input().split())) # 정답 10개 배열로 정리
back(0) # 0개부터 시작 - 왜냐? n+1로 1개씩 정답 추가할 예정이기 때문
print(cnt)