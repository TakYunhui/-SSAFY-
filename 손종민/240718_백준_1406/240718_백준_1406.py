# 커서
import sys
sys.stdin = open('input.txt')

word = list(input())
M = int(input())
after_cursor = []

for _ in range(M):
    order = list(input().split(' '))
    if order[0] == 'P':
        word.append(order[1])
    elif len(word) > 0 and order[0] == 'L':
        tmp = word.pop()
        after_cursor.append(tmp)
    elif len(after_cursor) > 0 and order[0] == 'D' :
        tmp = after_cursor.pop()
        word.append(tmp)
    elif len(word) > 0 and order[0] == 'B':
        word.pop()
    
    # print('단어', word)
    # print('커서 후', after_cursor)

word = word + after_cursor[::-1]
print(''.join(word))