# 풀이 날짜 : 2023.12.20
# 문제 유형 : 연습문제
# 문제 제목 : 멀리 뛰기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12914

def solution(n):
    # 피보나치 수열
    # n = 1: 1 => 1
    # n = 2: 11 2 => 2
    # n = 3: 111 12 21 => 3
    # n = 4: 1111 121 112 211 22 => 5
    # n = 5: 11111 2111 1211 1121 1112 221 212 122 => 8
    # n = 6: 111111 21111 12111 11211 11121 11112 2211 2121 2112 1212 1122 1221 222 => 13

    a, b = 0, 1

    for i in range(1, n + 1):
        a, b = b, a + b

    return b % 1234567
