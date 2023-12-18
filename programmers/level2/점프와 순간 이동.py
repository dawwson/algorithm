# 풀이 날짜 : 2023.12.18
# 문제 유형 : Summer/Winter Coding(~2018)
# 문제 제목 : 점프와 순간 이동
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12980

def solution(n):
    usage = 0

    while n != 0:
        # 2로 나누어 떨어지면 건전지 소모가 없음
        if n % 2 == 0:
            n /= 2
        # 2로 나누어 떨어지지 않으면 한 칸 이동해야 함
        else:
            n -= 1
            usage += 1
    return usage
