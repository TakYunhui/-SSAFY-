import sys
from collections import defaultdict
sys.stdin = open('input.txt')

N = int(input())

ls = list(input())

labels = ['*', '-', '+', '/']

ls_num = defaultdict(int)



for item in ls:
    if item not in labels and item not in ls_num:
        ls_num[item] = int(input())


print(ls_num)