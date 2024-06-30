import sys

sys.stdin = open('input.txt')


caseNumber = input()
numberList = []
originNumber = []

for number in caseNumber:
    numberList.append(int(number))

for i in range(len(numberList)):
    # print(i)
    if i == 0:
        # 맨 처음 숫자가 0이라면, 실제 숫자는 1보다 커야 하므로 10을 더하기
        if numberList[i] == 0:
            originNumber.append(numberList[i] + 10)
        # 0 아니면 그냥 넣기
        else:
            originNumber.append(numberList[i])
        # print(originNumber)
    else:
        # 첫 숫자가 아니면 직전 숫자 뒷자리와 비교해야 함

        # 현재 숫자가 앞 숫자의 뒷자리보다 크면
        # 앞숫자 10의 자리 만큼 더해줘야 함
        if numberList[i] > originNumber[-1] % 10:
            originNumber.append(numberList[i] +(10 * (originNumber[-1] // 10)))
        # 현재 숫자가 앞 숫자 뒷자리보다 작으면
        # 앞숫자보다 한 자리 더 올려줘야 함
        else:
            case1 = numberList[i] + (10 * (originNumber[-1] // 10 + 1))
            case2 = numberList[i] * 10
            if case1 > case2 and case2 > originNumber[-1]:
                originNumber.append(case2)
            else:
                originNumber.append(case1)
    print(originNumber)



print(max(originNumber))