# N과 M(2) # 230711

# 1부터 N 까지 자연수 중 중복없이 M개를 고른 수열
# 고른 수열은 오름차순

# 조합구하기...음..8까지니까 브루트포스나 백트래킹
# 백트래킹이군..? 못하겠다.

# 0715 다시 도전

N, M = map(int, input().split())
arr = []

def back(n, list_n, length):
    # 종료 조건
    if (length==M):
        for atom in list_n:
            print(atom, end=' ')
        print()
        return
    # 아닐 경우
    else:
        for i in range(n+1, N+1):
            # 사용하는 경우
            list_n.append(i)
            back(i, list_n, length+1)
            # 아닌 경우
            list_n.pop()
            back(i, list_n, length)


if (M==1):
    for i in range(1, N+1):
        print(i)
else:
    back(0, arr, 0)
# 재귀로 한개뽑고 으음
