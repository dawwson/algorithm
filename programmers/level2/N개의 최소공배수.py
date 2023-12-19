# 풀이 날짜 : 2023.12.19
# 문제 유형 : 연습문제
# 문제 제목 : N개의 최소공배수
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):

    lcm = arr[0]

    for num in arr[1:]:
        # 최소공배수는 두 자연수의 곱을 최대공약수로 나눈 값이다.
        # 리스트를 순회하면서, 최소공배수와 자연수의 곱을 최대공약수로 나눈 값이 새로운 최소공배수가 된다.
        # // : 정수 나눗셈(소수점 버림. 결과값 정수)
        # /  : 실수 나눗셈(소수점 있음. 결과값 실수)
        lcm = lcm * num // gcd(lcm, num)

    return lcm


def gcd(a, b):
    # 유클리드호제법 : a와 b의 최대공약수는 (a를 b로 나눈 나머지)와 (b)의 최대공약수이다.
    # python math.gcd(a, b)로도 대체 가능
    if b == 0:
        return a
    return gcd(b, a % b)
