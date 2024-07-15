# N과 M (4)

# 같은 수 여러번 골라도 됨
# 비내림 차순
# 중복순열

def back(n, length, list_n):
    if (length == M):
        # 출력
        for num in list_n:
            print(num, end=' ')
        print()
    else:
        for i in range (n, N+1):
            if (len(list_n)!=0 and i < list_n[-1]):
                pass
            else:
                list_n.append(i)
                back(n, length+1, list_n)
                list_n.pop()

N, M = map(int, input().split())
arr = []

back(1, 0, arr)