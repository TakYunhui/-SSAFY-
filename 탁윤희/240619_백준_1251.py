# 실버 5: 단어 나누기
word = list(input())
result = [] # 경우의 수를 담을 리스트

# 쪼개지는 모든 단어의 경우의 수 구하기
for i in range(1, len(word) - 1): # 각 단어가 적어도 1개 이상의 길이를 가지도록 함
    for j in range(1+i, len(word)): # i에 1을 더해줘야 0개 길이의 단어가 안 나온다
        first = word[:i]
        second = word[i:j]
        third = word[j:]

        # 뒤집기
        first.reverse()
        second.reverse()
        third.reverse()

        result.append("".join(first + second + third))

# 사전 순으로 가장 앞선 단어 출력
# == 리스트의 가장 작은 값 출력하기 (사전순서로 읽어온다)
print(min(result))
