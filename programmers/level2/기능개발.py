# 풀이 날짜 : 2023.12.14
# 문제 유형 : 스택/큐
# 문제 제목 : 기능개발
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math

def solution(progresses, speeds):
    days = []

    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100 - progress) / speed)
        days.append(day)

    front = 0
    deploy_cnt = []

    for day in days:
        if not deploy_cnt or day > front:
            deploy_cnt.append(1)
            front = day
        else:
            deploy_cnt[-1] += 1

    return deploy_cnt
