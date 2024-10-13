# A에서 모든 숫자가 나누어지고, B에서 모든 숫자를 나눌 수 없을 때.
# 배열 길이가 같으므로 두 배열을 for문 돌리기보다는 인덱스로 접근하자
# arrayA가 철수 arrayB가 영희

def solution(arrayA, arrayB):
    answer = 2
    isAnswer = False
    isChulsoo = False
    isYounghee = False
    while isAnswer == False:
        # 철수로 나누고 있고, 가장 작은 원소 넘으면 못 찾은 것이므로 멈추기
        if isChulsoo == True and answer > arrayA[0]:
            answer = 0
            break
        # 영희로 나누고 있고, 가장 작은 원소 넘으면 못 찾은 것이므로 멈추기
        elif isYounghee == True and answer > arrayB[0]:
            answer = 0
            break
        # 두 조건 아닌 경우 answer 기반으로 진행
        for i in range(len(arrayA)):
            # 둘 다 나눠질 경우 조건이 해당되지 않으므로 초기화하고 다음 값으로
            if arrayA[i] % answer == 0 and arrayB[i] % answer == 0:
                isChulsoo = False
                isYounghee = False
                isAnswer = False
                break
            # 둘 다 나눠지지 않을 경우에도 초기화하고 다음 값으로
            elif arrayA[i] % answer != 0 and arrayB[i] % answer != 0:
                isChulsoo = False
                isYounghee = False
                isAnswer = False
            # 철수가 나눠질 경우
            elif arrayA[i] % answer == 0 and arrayB[i] % answer != 0:
                # 영희가 활성화되어 있는 거라면 멈춰야함
                if isYounghee == True:
                    isYounghee = False
                    isAnswer = False
                    break
                else:
                    isAnswer = True
                    isChulsoo = True
            elif arrayA[i] % answer != 0 and arrayB[i] % answer == 0:
                if isChulsoo == True:
                    isChulsoo = False
                    isAnswer = False
                    break
                else:
                    isAnswer = True
                    isYounghee = True
        # 모든 조건 통과시
        if isAnswer == True:
            print('조건 통과!')
            # while문 멈추기
            break
        # 못찾은 채로 for문이 끝난다면
        else:
            answer += 1
    return answer

arrayA = [10, 17]
arrayB = [5, 20]

print(solution(arrayA, arrayB))