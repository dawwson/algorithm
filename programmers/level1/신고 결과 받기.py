# 풀이 날짜 : 2023.12.11
# 문제 유형 : 2022 KAKAO BLIND RECRUITMENT
# 문제 제목 : 신고 결과 받기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 신고된 아이디: 신고된 횟수
    reported_list = {x: 0 for x in id_list}

    # 중복 신고 제거하기 위해 set 사용
    for r in set(report):
        reporter, reported = r.split()
        reported_list[reported] += 1

    for r in set(report):
        reporter, reported = r.split()

        if reported_list[reported] >= k:
            answer[id_list.index(reporter)] += 1

    return answer
