# 실버 2 . 한 줄로 서기
# 각 순서 마다 자기보다 키 큰 사람이 왼쪽에 있는 수를 받음 => 오른쪽에 키큰 사람 있는 건 신경x
# 키가 큰 수부터 역으로 넣어준다
n = int(input())
arr = list(map(int, input().split()))
cm = list(range(1, n+1))
result = []
j = -1
for i in range(n):
    result.insert(arr[j], cm[j])
    j-=1


for i in result:
    print(i, end=' ')