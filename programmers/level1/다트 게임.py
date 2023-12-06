# 풀이 날짜 : 2023.12.06
# 문제 유형 : 2018 KAKAO BLIND RECRUITMENT
# 문제 제목 : 다트게임
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    rules = {'S': 1, 'D': 2, 'T': 3}
    results = []

    score = ''

    for c in dartResult:
        if c.isdigit():
            score += c
            continue
        if c in rules:
            results.append(int(score) ** rules[c])
            score = ''
            continue
        if c == '*':
            if len(results) == 1:
                results[0] *= 2
                continue
            if len(results) > 1:
                results[-1] *= 2
                results[-2] *= 2
                continue
        if c == '#':
            results[-1] *= -1
            continue

    return sum(results)
