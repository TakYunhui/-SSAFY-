import sys
sys.stdin = open('input.txt')

string = list(input())
print(string)

cnt_b = 0
result = 0
for i in range(len(string)):
    if string[i] == 'b':
        cnt_b += 1
        # 한번 이상으로 세어졌으면
        if i != len(string) and string[i+1] == 'a':
            for j in range(i+ 1, len(string)):
                if string[j] == 'b':
                    string[i+1] = 'b'
                    string[j] = 'a'
                    result += 1
                    print(string)
                    break

print(result)
