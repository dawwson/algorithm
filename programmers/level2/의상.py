# 풀이 날짜 : 2023.12.15
# 문제 유형 : 해시
# 문제 제목 : 의상
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

import math


def solution(clothes):
    count = 1
    types = {}

    for cloth in clothes:
        if cloth[1] in types:
            types[cloth[1]].append(cloth[0])
        else:
            types[cloth[1]] = [cloth[0]]

    for value in types.values():
        # 안 입는 경우를 포함하여 조합의 수를 구한다.
        count *= len(value) + 1

    # 아무것도 안 입는 경우의 수를 뺀다.
    return count - 1
