# 풀이 날짜 : 2023.12.11
# 문제 유형 : 2022 KAKAO TECH INTERNSHIP
# 문제 제목 : 성격 유형 검사하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    types = {
        'R': 0, 'T': 0,
        'C': 0, 'F': 0,
        'J': 0, 'M': 0,
        'A': 0, 'N': 0
    }

    for index, choice in enumerate(choices):
        type1, type2 = list(survey[index])
        if choice == 1:
            types[type1] += 3
        if choice == 2:
            types[type1] += 2
        if choice == 3:
            types[type1] += 1
        if choice == 5:
            types[type2] += 1
        if choice == 6:
            types[type2] += 2
        if choice == 7:
            types[type2] += 3

    if types['R'] < types['T']:
        answer += 'T'
    else:
        answer += 'R'

    if types['C'] < types['F']:
        answer += 'F'
    else:
        answer += 'C'

    if types['J'] < types['M']:
        answer += 'M'
    else:
        answer += 'J'

    if types['A'] < types['N']:
        answer += 'N'
    else:
        answer += 'A'

    return answer
