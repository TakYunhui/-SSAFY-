# 20125 쿠키의 신체 측정

import sys

sys.stdin = open('input.txt')

N = int(input())

cookie = []


for i in range(N):
    line = input()
    tmp = []
    for word in line:
        tmp.append(word)
    cookie.append(tmp)

heartX = 0
heartY = 0

for i in range(N):
    heartY = i + 2
    if '*' in cookie[i]:
        heartX = cookie[i].index('*') + 1
        break

# 왼팔 찾기
leftHandLength = 1
while heartX - 2 - leftHandLength >= 0: 
    # print(heartY - 1)
    # print(heartX - 1 - length)
    # print(cookie[heartY - 1][heartX - 1 - length])
    if cookie[heartY - 1][heartX - 2 - leftHandLength] == '_':
        # print('도착')
        break
    else:
        leftHandLength += 1

rightHandLength = 1
while heartX + rightHandLength + 1 <= N:
    if cookie[heartY - 1][heartX + rightHandLength] == '_':
        break

    else:
        rightHandLength += 1


waistLength = 1
while cookie[heartY + waistLength][heartX - 1] == '*':
    waistLength += 1

leftLegLength = 1
while heartY + waistLength + leftLegLength  + 1 <= N:
    if cookie[heartY + waistLength + leftLegLength ][heartX - 2] == '_':
        break
    else:
        leftLegLength  += 1

rightLegLength = 1
while heartY + waistLength + rightLegLength + 1 <= N:
    if cookie[heartY + waistLength + rightLegLength][heartX] == '_':
        break
    else:
        rightLegLength += 1

print(heartY, heartX)
print(leftHandLength, rightHandLength, waistLength, leftLegLength, rightLegLength)