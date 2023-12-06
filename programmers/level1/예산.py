# 풀이 날짜 : 2023.12.06
# 문제 유형 : Summer/Winter Coding(~2018)
# 문제 제목 : 예산
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    # 오름차순 정렬 후 적은 예산부터 제외시키면 부서를 최대로 나눠줄 수 있음
    for amount in sorted(d):
        if budget - amount >= 0:
            budget -= amount
            answer += 1
    return answer
