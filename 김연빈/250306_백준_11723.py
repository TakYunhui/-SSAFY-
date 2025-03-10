# 11723 # 250306
# 시간 초과
# fastio 사용하면 valueError가 남
import sys
input=sys.stdin.readline

s = set()
all_S = {i for i in range(1, 21)}
# print(all_S)
n = int(input())

for _ in range(n):
    cal = input()
    cal = cal.strip('\n')
    if (cal =="all"):
        s = all_S | s
    elif (cal == "empty"):
        s.clear()
    else:
        command, num = cal.split()
        num = int(num)
        if (command == "add"):
            s.add(num)
        elif (command == "remove"):
            s.discard(num)
        elif (command == "check"):
            print(int(num in s))
        elif (command == "toggle"):
            if num in s:
                s.discard(num)
            else:
                s.add(num)
    # print(command, num)
