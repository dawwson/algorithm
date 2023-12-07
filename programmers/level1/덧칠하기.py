# 풀이 날짜 : 2023.12.07
# 문제 유형 : 연습문제
# 문제 제목 : 덧칠하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    paint_count = 1
    prev = section[0]

    for s in section:
        if s - prev >= m:
            paint_count += 1
            prev = s

    return paint_count
