# 풀이 날짜 : 2023.11.30
# 문제 유형 : 완전탐색
# 문제 제목 : 최소직사각형
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_list = []
    min_list = []

    # 명함을 회전시킬 수 있으므로 긴 쪽/짧은 쪽을 나눠서 배열에 저장한다.
    for s in sizes:
        max_list.append(max(s))
        min_list.append(min(s))

    # 긴 쪽 중에 최댓값 * 짧은 쪽 중에 최댓값이 지갑의 최소 크기이다.
    return max(max_list) * max(min_list)