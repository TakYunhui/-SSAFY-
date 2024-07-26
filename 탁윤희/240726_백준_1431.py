# 실버 3. 시리얼 번호
# A, B - 길이가 다르면 짧은 것 우선
# 길이가 같으면 A 모든 자리수 합 / B 모든 자리수 합 비교 -> 작은 합
# 위 조건으로 비교 안 되면 사전순 (알파벳보다 숫자가 작음)
n = int(input())
codes = list()
for i in range(n):
    codes.append(input())

def sum_num(x):
    result = 0
    for i in x:
        if i.isdigit():
            result += int(i)
    return result

# 길이순, 합, 문자열 순 기준으로 정렬
codes.sort(key=lambda x:(len(x), sum_num(x), x))
for i in codes:
    print(i)