# 통계학

N = int(input())

arr = []
total = 0
nums = dict()
often = (1, 0)

for i in range(N):
    num = int(input())
    arr.append(num)
    total += num
    tmp = nums.get(num)
    if (i == 0):
        often = (1, num)
    if (tmp==None):
        nums[num] = 1
    else:
        nums[num] = tmp+1
        if (tmp+1 > often[0]):
            often = (tmp+1, num)
        

arr.sort()

print(round(total/N))
print(arr[N//2]) # 중앙
print(often[1]) # 최빈
print(arr[-1]-arr[0]) # 범위