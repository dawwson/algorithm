# 풀이 날짜 : 2023.12.15
# 문제 유형 : 2018 KAKAO BLIND RECRUITMENT
# 문제 제목 : [1차] 캐시
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17680

def solution(cacheSize, cities):
    # 캐시를 사용하지 않으면 DB로 접근
    if cacheSize == 0:
        return 5 * len(cities)

    # 사용된지 오래된 순으로 정렬됨
    cache = []
    time = 0

    for city in cities:
        city = city.lower()

        # cache hit
        if city in cache:
            time += 1
            # 사용된 값을 맨 뒤로 보냄
            used = cache.pop(cache.index(city))
            cache.append(used)
        # cache miss
        else:
            time += 5
            # 캐시에 남은 용량이 없으면 가장 오래된 데이터 삭제
            if len(cache) == cacheSize:
                cache = cache[1:]
            cache.append(city)
    return time
