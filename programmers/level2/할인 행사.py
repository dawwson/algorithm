# 풀이 날짜 : 2023.12.26
# 문제 유형 : 연습문제
# 문제 제목 : 할인 행사
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131127


def solution(want, number, discount):
    discount_cnt = 0

    while len(discount) >= len(want):
        all_discounted = True

        for w, n in zip(want, number):
            if discount[0:10].count(w) < n:
                all_discounted = False
                break
        if all_discounted:
            discount_cnt += 1
        discount.pop(0) # 슬라이싱할 경우 시간초과됨

    return discount_cnt
