# 좌표 압축

# Xi > Xj를 만족하는 Xj 개수 구하기

# 브루트포스로 풀기에 N이 너무 큼

N = int(input())
arr = list(map(int, input().split()))

# 중복없는 배열로 만들고 정렬하면 해당 인덱스가 압축된 좌표임
# 이걸 dict로 만들면 되지않을까?
# 검색했는데 제목만 봤음

new_arr = sorted(list(set(arr)))
new_dict = {}
for i in range(len(new_arr)):
    new_dict[new_arr[i]] = i

for num in arr:
    print(new_dict[num], end=' ')