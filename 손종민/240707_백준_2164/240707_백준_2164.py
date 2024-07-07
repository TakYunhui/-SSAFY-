import sys

sys.stdin = open('input.txt')

from collections import deque

N = int(input())

cards = deque(range(1, N + 1))

while len(cards) > 1:
    cards.popleft()
    cards.append(cards.popleft())
    # print(cards)

print(cards[0])