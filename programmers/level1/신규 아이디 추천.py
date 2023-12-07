# 풀이 날짜 : 2023.12.07
# 문제 유형 : 2021 KAKAO BLIND RECRUITMENT
# 문제 제목 : 신규 아이디 추천
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/72410

import re


def solution(new_id):
    result1 = step1(new_id)
    result2 = step2(result1)
    result3 = step3(result2)
    result4 = step4(result3)
    result5 = step5(result4)
    result6 = step6(result5)
    result7 = step7(result6)
    return result7


def step1(s):
    # 모든 대문자를 대응되는 소문자로 치환
    return s.lower()


def step2(s):
    # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    return re.sub(r'[^a-z0-9\-_\.]', '', s)


def step3(s):
    # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    return re.sub(r'\.{2,}', '.', s)


def step4(s):
    # 마침표(.)가 처음이나 끝에 위치한다면 제거
    return re.sub(r'^\.|\.+$', '', s)


def step5(s):
    # 빈 문자열이라면, new_id에 "a"를 대입
    if not s:
        return 'a'
    return s


def step6(s):
    # 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    if len(s) > 15:
        sliced = s[:15]
        # 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거
        if sliced[-1] == '.':
            return sliced[:14]
        return sliced
    return s


def step7(s):
    # 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    if len(s) <= 2:
        repeated = s[-1] * (3 - len(s))
        return s + repeated
    return s
