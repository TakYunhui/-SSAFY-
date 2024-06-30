# 실버 5 : 올림픽
# 1. 금메달 수 2. 은메달 수 3. 동메달 수
# 동일한 메달 수 = 같은 순위, 다음 국가는 같은 순위수들 다음
# => 금, 은, 동 개수 대로 정렬 후 순위 매기기
n, k = map(int, input().split()) # 국가 수 n, 등수 알 국가 순서 k
# 메달 수 받기
medals = [list(map(int, input().split())) for i in range(n)]
# 메달 수에 따른 정렬
medals.sort(key = lambda x : (-x[1], -x[2], -x[3]))
# 찾고 있는 국가의 인덱스 확인 => 처음에 정렬된 거에서 바로 k로 찾으려 함;
idx = [medals[i][0] for i in range(n)].index(k)
# 순위 매기기
for i in range(n):
    # 해당 인덱스와 메달 수가 동일한 국가를 찾아 인덱스 + 1(등수) 출력
    # +1 의 이유 : 1등이 인덱스 0이므로 +1 함
    if medals[idx][1:] == medals[i][1:]:
        print(i+1)
        break

