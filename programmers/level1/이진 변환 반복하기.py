# 풀이 날짜 : 2023.12.12
# 문제 유형 : 월간 코드 챌린지 시즌 1
# 문제 제목 : 이진 변환 반복하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    if s == '1':
        return [0, 0]

    convert_count = 0
    zero_count = 0

    while s != '1':
        convert_count += 1
        zero_count += s.count('0')

        s = s.replace('0', '')
        s = bin(len(s))[2:]

    return [convert_count, zero_count]
