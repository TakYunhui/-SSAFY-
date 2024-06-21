# 실버 5 : 논리학 교수
# 정확하게 i 개의 말은 참이다 - 라는 내용이 i개 있어야 i개가 참이 된다
# 각 말의 빈도수를 측정
n = int(input())
arr = list(map(int, input().split()))

result = -1 # 빈도 수 맞는 게 없다면 모순(-1) 출력
for i in range(n+1):
    true_cnt = arr.count(i) # i가 몇 개 나오는지 빈도수 측정
    if true_cnt == i:
        result = max(result, i)

print(result)

# 문제 이해 자체를 잘 하지 못 했다 ;