# 풀이 날짜 : 2023.12.22
# 문제 유형 : 연습문제
# 문제 제목 : 연속 부분 수열의 합의 개수
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    sum_set = set()

    # x : 연속 부분 수열의 길이
    for l in range(1, len(elements)+1):
        # 연속 부분 수열의 시작 인덱스
        for start in range(len(elements)):
            subtotal = 0

            if start+l > len(elements):
                subtotal = sum(elements[start:] + elements[:start+l-len(elements)])
            else:
                subtotal = sum(elements[start:start+l])

            sum_set.add(subtotal)

    return len(sum_set)
