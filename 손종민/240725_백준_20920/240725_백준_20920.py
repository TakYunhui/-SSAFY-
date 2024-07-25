import sys
sys.stdin = open('input.txt')

from collections import defaultdict
N, M = map(int, input().split(' '))

words = defaultdict(int)
for _ in range(N):
    current_word = input()
    if len(current_word) >= M:
        words[current_word] += 1       

word_keys = list(words.keys())
word_keys.sort(key = lambda x : (-words[x], -len(x), x))
# print(word_keys)
for word in word_keys:
    print(word)