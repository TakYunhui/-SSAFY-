# 풀이 참고
# 이렇게 해도 시간초과
# sys 해야되나봄
# 다른풀이도 찾아보기

n = int(input())
data = []

total = 0
count = dict()

for _ in range(n):
    x = int(input())
    data.append(x)

    total += x

    if x not in count:
        count[x] = 1
    else:
        count[x] += 1

data.sort()

print(round(total/n))
print(data[n//2]) # 중앙

# 최빈
# 여기가 중요한듯
freq = max(count.values())
nums = []
for key, val in count.items():
    if val == freq:
        nums.append(key)
if len(nums) == 1:
    print(nums[0])
else:
    print(sorted(nums)[1])

print(data[-1]-data[0]) # 범위