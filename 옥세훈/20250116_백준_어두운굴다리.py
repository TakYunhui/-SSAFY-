n = int(input())
m = int(input())
x = list(map(int, input().split()))

first = x[0]
last = n - x[-1]
  
max_val = 0
for i in range(m-1):
    check = x[i+1] - x[i]
    if check > max_val:
      max_val = check
mid = 0
if max_val % 2 == 0:
  mid = max_val // 2
else:
  mid = max_val // 2 + 1
  
print(max(first, mid , last))