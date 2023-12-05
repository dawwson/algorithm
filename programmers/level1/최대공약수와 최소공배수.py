# 풀이 날짜 : 2023.11.28
# 문제 유형 : 연습문제
# 문제 제목 : 최대공약수와 최소공배수
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, m):
    # 최소공배수는 두 정수의 곱을 최대공약수로 나눈 값이다.
    # lcm = n * m / gcd
    gcd = getGcd(n, m)
    lcm = n * m / gcd
    return [gcd, lcm]


def getGcd(a, b):
    # 유클리드호제법 : a와 b의 최대공약수는 a를 b로 나눈 나머지와 b의 최대공약수이다.
    if b == 0:
        return a
    return getGcd(b, a % b)
