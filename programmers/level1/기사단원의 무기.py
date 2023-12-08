# 풀이 날짜 : 2023.12.08
# 문제 유형 : 연습문제
# 문제 제목 : 기사단원의 무기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/136798
def solution(number, limit, power):
    # 1번 기사 제외하고 시작
    weight = 1

    for n in range(2, number + 1):
        # 1과 자기 자신은 포함
        divisor_count = 2

        for i in range(2, int(n**(1/2)) + 1):
            if n % i == 0:
                divisor_count += 1
                if i**2 != n:
                    divisor_count += 1

        if divisor_count > limit:
            weight += power
        else:
            weight += divisor_count

    return weight
