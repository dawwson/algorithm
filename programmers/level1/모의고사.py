# 풀이 날짜 : 2023.11.30
# 문제 유형 : 완전탐색
# 문제 제목 : 모의고사
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    # 각 수포자의 정답 패턴을 저장한 배열
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    scores = [0, 0, 0]
    result = []

    for index, answer in enumerate(answers):
        # 패턴의 길이만큼 끊어서 정답을 체크한다.
        if answer == pattern1[index % len(pattern1)]:
            scores[0] += 1
        if answer == pattern2[index % len(pattern2)]:
            scores[1] += 1
        if answer == pattern3[index % len(pattern3)]:
            scores[2] += 1

    # 가장 많이 맞춘 학생들만 저장한 배열을 반환한다.
    for index, score in enumerate(scores):
        if score == max(scores):
            result.append(index + 1)
    return result
