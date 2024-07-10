# 실버 3 타노스
# 절반의 0과 1을 제거해 새로운 문자열 s'
# 사전순으로 가장 빠른 s'?
# 1010 -> 1, 0 => 01
# 000011 -> 001 => 001
# 즉, 무조건 0과 1을 각각 절반으로 줄인다
# 이때, 나오는 조합 중 사전순으로 가장 빠른 것 (위치의 재배치는 x)
s = input()
# 존재할 수 있는 0과 1의 개수
zero = s.count("0") // 2
one = s.count("1") // 2
result = list(s)

while zero or one:
    if one:
        result.remove("1")
        one -= 1
    elif zero:
        result.reverse()
        result.remove("0")
        result.reverse()
        zero -= 1

print("".join(result))


