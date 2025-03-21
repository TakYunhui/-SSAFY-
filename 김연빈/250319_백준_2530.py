# 색종이 만들기
# N = int(input())
# papers = []
# for _ in range(N):
#     row = list(map(int, input().split()))
#     papers.append(row)

# is_white = False
# is_blue = False
# is_one = True
# blue_cnt = 0
# white_cnt = 0
# for i in range(N):
#     for j in range(N):
#         if (i==0 and j==0):
#             if (papers[i][j]==1):
#                 is_blue = True
#             else:
#                 is_white = True
#         else:
#             if (is_blue==True):
#                 if (papers[i][j]==0):
#                     is_one = False
#                     break
#     if (is_one==False):
#         break
# if (is_one):
#     if (is_blue):
#         blue_cnt += 1
#     else:
#         white_cnt += 1
# ---위에 얘네를 함수로 만들면 뭔가 될것같은데..시작, 끝을 파라미터로 주고? > 근데 하기싫다..모르겠다..
# 사분면 나누는거 생각해서 함수 만들어보자

# 정답코드
# 출처: https://edder773.tistory.com/116 [개발하는 차리의 학습 일기:티스토리]
def div(y, x, n): 
    color = paper[y][x] # 색종이의 색
    for i in range(y, y+n): # y 분할 
        for j in range(x, x+n): # x 분할
            if color != paper[i][j]: # 찾는 과정에서 색이 달라지면
                m = n//2
                div(y, x, m) # 색종이 분할 (2사분면)
                div(y, x + m, m) # 색종이 분할 (1사분면)
                div(y + m, x, m) # 색종이 분할 (3사분면)
                div(y + m, x + m, m) # 색종이 분할(4사분면)
                return
    if color == 0: # 흰색이면
        result[0] += 1 #자르기
    else : # 파란색이면
        result[1] += 1 # 갯수세기
        
import sys
N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 색종이
result = [0,0] # 자른 색종이 / 파란색 색종이
div(0,0,N)
print(result[0],'\n',result[1],sep='')