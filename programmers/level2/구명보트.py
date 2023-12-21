# 풀이 날짜 : 2023.12.20
# 문제 유형 : 탐욕법(Greedy)
# 문제 제목 : 구명보트
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    # 오름차순 정렬
    people.sort()
    # 가장 적게 나가는 사람 + 가장 많이 나가는 사람 태우기
    count = 0
    start = 0
    end = len(people) - 1

    while start < end:
        if people[start] + people[end] > limit:
            # 무거운 사람만 태움
            end -= 1
        else:
            # 둘 다 태움
            start += 1
            end -= 1
        count += 1

        # 마지막 한 명이 남으면 태움
        if start == end:
            count += 1
    return count
