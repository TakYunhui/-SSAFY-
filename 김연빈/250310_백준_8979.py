# 8979 올림픽 # 250310
nation_list = []
n, k = map(int, input().split())
for _ in range(n):
    i, g, s, b = list(map(int, input().split()))
    new_nation = list([g, s, b, i])
    nation_list.append(new_nation)

nation_list.sort(reverse=True)

# print(nation_list)

rank = 1
for i in range(n):
    if (i!=0):
        if (nation_list[i-1][0:3]!=nation_list[i][0:3]):
            rank = i+1
    if (k==nation_list[i][3]):
        #  find
        print(rank)
        break
