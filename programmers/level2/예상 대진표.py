# 풀이 날짜 : 2023.12.21
# 문제 유형 : 2017 팁스타운
# 문제 제목 : 예상 대진표
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12985

import math


def solution(n, a, b):
    # 라운드 수 = 로그 2(밑)의 n
    for r in range(1, int(math.log(n, 2))+1):
        # 두 번호의 차이가 1이면서 큰 쪽이 짝수일 때 만남
        if abs(a-b) == 1 and max(a, b) % 2 == 0:
            return r
        else:
            # 짝수 : n/2번으로 올라감
            # 홀수 : (n+1)/2 번으로 올라감
            if a % 2 == 0:
                a = a // 2
            else:
                a = (a + 1) // 2
            if b % 2 == 0:
                b = b // 2
            else:
                b = (b + 1) // 2
