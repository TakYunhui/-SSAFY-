# 브론즈 1 : 명령 프롬프트
n = int(input())

names = [list(input()) for i in range(n)]
result = names[0]
word_length = len(result)

for i in range(1, n):
    name = names[i]
    for j in range(word_length):
        if name[j] != result[j]:
            result[j] = "?"

print(''.join(result))