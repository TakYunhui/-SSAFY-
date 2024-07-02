# 20310 타노스

import sys

sys.stdin = open('input.txt')

# input 받아와서
# 0과 1을 분리해서 저장한 뒤
# 절반 개수의 0을 출력하고, 그 뒤 절반 개수의 1 출력

# 반례 : 0이 나왔다 1이 나왔다 다시 0이 나오는 경우

# 순회해서 0은 뒤에서부터 지우기, 1은 앞에서부터 지우기


N = list(input())
zeros = N.count('0')
ones = N.count('1')

# print(zeros)
# print(ones)
# print(N)
# 전체 문자열 순회하면서
for _ in range(zeros // 2) :
    # print(N[::-1])
    # print(-N[::-1].index('0')-1)
    # 인덱스를 뒤에서부터 순회하면 -1이 붙으므로
    # -N[::-1]에서 추가로 1을 더 빼주어야 인덱스가 맞음. 
    N.pop(-(N[::-1].index('0')) - 1)
for _ in range(ones // 2) :
    N.pop(N.index('1'))

result = ""

# 문자열을 출력할 때에는 .join 메서드를 쓰자
print(result.join(N))