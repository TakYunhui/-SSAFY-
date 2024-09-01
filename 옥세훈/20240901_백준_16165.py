import sys
input = sys.stdin.readline

n, m = map(int, input().split())

all_girls = dict()
for _ in range(n):
    name = input().rstrip()
    num = int(input())
    girls = []

    for i in range(num):
        girl_name = input().rstrip()
        girls.append(girl_name)

    all_girls[name] = girls

# print(all_girls)
for _ in range(m):
    quiz = input().rstrip()
    quiz_num = int(input())

    if quiz_num:
       for x, y in all_girls.items():
           if quiz in y:
               print(x)
               break
    else:
        check = all_girls.get(quiz)
        check.sort()
        for i in check:
            print(i)