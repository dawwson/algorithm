# 풀이 날짜 : 2024.01.02
# 문제 유형 : 2022 KAKAO BLIND RECRUITMENT
# 문제 제목 : k진수에서 소수 개수 구하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92335

def solution(n, k):
    global formatted
    formatted = ''

    # k 진수로 변환
    recursive_k(n, k)
    # '0'을 기준으로 나눈다.
    words = formatted.split('0')

    # 소수의 개수 찾기
    count = 0

    for word in words:
        # 빈 문자열이면 PASS
        if len(word) == 0:
            continue

        n = int(word)
        if is_prime(n):
            count += 1

    return count


def recursive_k(n, k):
    global formatted
    formatted = str(n % k) + formatted

    # 몫이 0이면 종료
    if n // k == 0:
        return
    recursive_k(n // k, k)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True
