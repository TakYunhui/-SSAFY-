# 영단어 암기는 괴로워

# 자주 나오면 앞
# 길면 앞
# 사전순
# 길이 M 이상

N, M = map(int, input().split())

word_note = dict()
final_note = []

for _ in range(N):
    word = input()
    if (len(word) < M):
        continue
    if (word_note.get(word)):
        word_note[word] += 1
    else:
        word_note[word] = 1

for word in word_note:
    final_note.append((word_note[word], word))

final_note.sort(key=lambda x:(-x[0], -len(x[1])))

for count, word in final_note:
    print(word)