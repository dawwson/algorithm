# 풀이 날짜 : 2023.12.21
# 문제 유형 : 연습문제
# 문제 제목 : 귤 고르기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter


def solution(k, tangerine):
    # {key: 사이즈, value: 개수}인 딕셔너리를 value 기준 내림차순 정렬
    sorted_items = sorted(Counter(tangerine).items(), key=lambda x: x[1], reverse=True)
    t_dict = dict(sorted_items)

    type_count = 0

    for size, count in t_dict.items():
        # 귤 개수를 채웠으면 종료
        if k <= 0:
            break
        # 한 종류로 귤 개수를 채울 수 있는 경우
        if count > k and type_count == 0:
            return 1

        k -= count
        type_count += 1

    return type_count
