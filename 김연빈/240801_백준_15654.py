# N과 M

N, M = map(int, input().split())

nums = list(map(int, input().split()))
check = [0] * N

nums.sort()

# 백트래킹
def back(step, arr):
    if (step == M):
        for num in arr:
            print(num, end=' ')
        print()
        return
    else:
        for i in range(N):
            # 사용한 경우
            if (check[i]==0):
                check[i] = 1
                back(step+1, arr+[nums[i]])
                check[i] = 0 # 아닌경우
                
back(0, [])
