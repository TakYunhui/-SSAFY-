N=int(input())
bild=[list(map(int,input().split())) for _ in range(N)]

bild.sort()

high_idx=0
high=0

for i in range(N):
    if(bild[i][1]>=high):
        high=bild[i][1]
        high_idx=i
sum=bild[high_idx][1]

start_h=bild[0][1]
for i in range(high_idx):   #높은 거 왼쪽
    if start_h < bild[i+1][1]:
        sum+=(bild[i+1][0]-bild[i][0])*start_h
        start_h=bild[i+1][1]
    else:
        sum+=(bild[i+1][0]-bild[i][0])*start_h

start_h=bild[N-1][1]
for i in range(N-1,high_idx,-1):    #높은 거 오른쪽
    if start_h < bild[i-1][1]:
        sum+=(bild[i][0]-bild[i-1][0])*start_h
        start_h=bild[i-1][1]
    else:
        sum+=(bild[i][0]-bild[i-1][0])*start_h

print(sum)