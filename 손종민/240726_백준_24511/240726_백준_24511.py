from collections import deque
import sys

sys.stdin = open('input.txt')

N = int(input())
que_or_stack = list(map(int, input().split(' ')))
