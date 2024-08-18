import sys

sys.stdin = open('input.txt')

n, m = map(int, input().split(' '))


result = []
for _ in range(n):
    people, limit = map(int, input().rstrip(' ').split(' '))
    mileges = list(map(int, input().rstrip(' ').split(' ')))
    mileges.sort(reverse=True)
    
    # 수강 가능 인원보다 신청 인원이 적은 경우
    if people < limit:
        # 마일리지 1만 넣기
        result.append(1)
    else:
        # 수강인원 맥시멈 인덱스에 있는 값을 넣어주면 됨
        result.append(mileges[limit-1])

# 최대한 많은 갯수를 세야 하므로 일단 정렬
result.sort()
count = 0

for i in result:
    if m - i >= 0:
        m -= i
        count += 1
    else:
        break

print(count)