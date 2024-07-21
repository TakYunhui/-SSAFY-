import sys
sys.stdin = open('input.txt')

T = int(input())
# 테스트케이스만큼 순회
for _ in range(T):
    n, k, t, m = map(int, input().split(' '))
    teamlist = []
    for i in range(n):
        team = {}
        team['id'] = i + 1
        team['point'] = [0] * (k+1)
        team['submit_count'] = 0
        team['last_submit'] = 0
        teamlist.append(team)
    # 로그 갯수만큼 순회
    total_submitted = 0
    for _ in range(m):
        total_submitted += 1
        log_entry = list(map(int, input().split(' ')))
        # 작으면 갱신
        if  teamlist[log_entry[0]-1]['point'][log_entry[1]] < log_entry[2]:
            teamlist[log_entry[0]-1]['point'][log_entry[1]] = log_entry[2]
        teamlist[log_entry[0]-1]['submit_count'] += 1
        teamlist[log_entry[0]-1]['last_submit'] = total_submitted

    teamlist.sort(key=lambda x : (-sum(x['point']), x['submit_count'], x['last_submit']))
    result = 0
    for i in range(len(teamlist)):
        if t == teamlist[i]['id']:
            result = i + 1
    print(result)