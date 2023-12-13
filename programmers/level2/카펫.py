# 풀이 날짜 : 2023.12.13
# 문제 유형 : 완전탐색
# 문제 제목 : 카펫
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    # 전체 면적
    area = brown + yellow

    # 최소 가로 길이부터 시작, 전체 면적의 제곱근까지 반복(정사각형)
    for n in range(3, int(area ** (1/2)) + 1):
        if area % n == 0:
            m = area / n
            # yellow 면적 = (w - 2) * (h - 2)
            if (n - 2) * (m - 2) == yellow:
                # 큰 쪽을 가로, 짧은 쪽을 세로로 설정
                return [max(n, m), min(n, m)]
