# 사람, 파티 수
N, M = map(int, input().split())
# 진실을 아는 사람 번호 목록
knows = set(input().split()[1:])
# 파티들
parties = [set(input().split()[1:]) for _ in range(M)]

for _ in range(M):
    for party in parties:
        # 파티 안에 진실을 아는 사람이 있다면
        if party & knows:
            # 진실을 아는 사람들 목록에 해당 파티 인원(set) 합치기
            knows = knows.union(party)

cnt = 0

for party in parties:
    # 만약 현재 파티에 진실을 아는 사람들이 있다면 넘어가기
    # & : intersection과 같은 역할?
    if party & knows:
        continue
    cnt += 1

print(cnt)