n = int(input())

halyGaly_ls = dict()
for _ in range(n):
    word, num = map(str, input().split())
    num = int(num)

    if not word in halyGaly_ls:
        halyGaly_ls[word] = num
    else:
        halyGaly_ls[word] += num

if 5 in halyGaly_ls.values():
    print("YES")
else:
    print("NO")

