# 듣도 못한 명단
# 보도 못한 명단
# 공통인 사람 찾기
# 2초
n, m = map(int, input().split())

ans = []
no_list = set()

# 해시에 저장하고
for _ in range(n):
    no_list.add(input())

# 있으면 +1
for _ in range(m):
    name = input()
    if (name in no_list):
        ans.append(name)

ans.sort()

print(len(ans))
for nono in ans:
    print(nono)