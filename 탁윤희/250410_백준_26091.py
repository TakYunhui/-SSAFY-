# 실버1. 현대모비스 소프트웨어 아카데미
# 학회원 수, 팀의 최소 능력치
n, m = map(int, input().split())
# 학회원 n명의 능력치
members = list(map(int, input().split()))
# 두 조건 만족 팀만 견학 가능
# 1. 팀원 2명
# 2. 모든 팀원 능력치 총합이 m이상
# => 최대 몇 팀 보낼 수 있을까?
# 팀원을 연속적으로 뽑으란 말이 없으니 정렬해도 됨
if n == 1:
    print(0)
else:
    members.sort()
    l, r = 0, n-1
    cnt = 0 # 팀 count할 변수
    while l < r:
        tmp = members[l] + members[r]
        if tmp >= m:
            cnt += 1
            l += 1
            r -= 1
        else:
            l += 1
    print(cnt)