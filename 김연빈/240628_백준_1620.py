# 나는야 포켓몬 마스터 이다솜

# 왜 시간초과? N, M은 100_000 이하 > pypy로 하면 됨

N, M = map(int, input().split())

pokemon_dict = dict()

for i in range(1, N+1):
    name = input()
    pokemon_dict[i] = name
    pokemon_dict[name] = i

print("dict: ", pokemon_dict)

for _ in range(M):
    find = input()
    if (find.isdigit()): # 문자열로 받기 때문에 그대로 딕셔너리에 검색하면 안나옴
        find = int(find)
    print(pokemon_dict.get(find))
    # print(poketmon_dict[find])
