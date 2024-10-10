from collections import deque


def solution(cacheSize, cities):
    # LRU : 적재 공간 중 가장 오래 참조되지 않은 페이지 교체
    # 참조 값이 캐시 안에 없으면 가장 오래 전에 참조한 페이지 빼고 넣기 (cache miss)
    # 반대로 참조 값이 캐시 안에 있으면 해당 값을 캐시 가장 최근에 넣기 (cache hit)
    answer = 0

    if cacheSize == 0:
        return 5 * len(cities)  # 캐시 크기가 0이면 무조건 miss

    cache = set()  # set으로 존재 확인 -> O(1)
    order = deque()  # 캐시 순서 관리

    for city in cities:
        city = city.lower()  # 대소문자 구별 x

        if city in cache:  # cache hit
            answer += 1
            order.remove(city)
            order.append(city)
        else:  # cache miss
            answer += 5
            if len(cache) >= cacheSize:
                # 가장 오래된 것(왼쪽) 제거
                cache.remove(order.popleft())
            cache.add(city)
            order.append(city)

    return answer