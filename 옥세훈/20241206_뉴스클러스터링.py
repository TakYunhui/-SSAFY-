import math

def solution(str1, str2):
    answer = 0
    
    str1 = str1.lower()
    str2 = str2.lower()
    # 두 집합의 교집합의 길이에, 합집합의 수를 나누는 것
    # 다중집합 = 원소의 중복을 허용함
    # 65536

    # 두 문자열을 집합으로 만들면 되는 듯
    # - 특수문자, 빈칸, 숫자 제거해야함 두개씩 확인하는데..
    # 자카드 유사도 계산하기
    
    a = []
    for i in range(len(str1)-1):
        check = str1[i:i+2]
        if check.isalpha():
            a.append(check)
        
    b = []
    for i in range(len(str2)-1):
        check1 = str2[i:i+2]
        if check1.isalpha():
            b.append(check1)
    
    if len(a) == 0 and len(b) == 0:
        return 65536
    
    a_temp = a.copy()
    a_result = a.copy()
    
    for i in b:
        if i not in a_temp:
            a_result.append(i)
        else:
            a_temp.remove(i)
    
    result = []
    for i in b:
        if i in a:
            a.remove(i)
            result.append(i)
            
    # print(a_result)
    # print(result)
    answer = math.trunc(len(result) / len(a_result) * 65536)
    return answer