# 풀이 날짜 : 2023.11.29
# 문제 유형 : 해시
# 문제 제목 : 완주하지 못한 선수
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42576

# pariticipant : 참가자 이름 배열
# completion : 완주자 이름 배열
def solution(participant, completion):
    hashDict = {}
    sumHash = 0

    # 참가자를 모두 딕셔너리(해시테이블)에 넣는다.
    for p in participant:
        hashDict[hash(p)] = p  # key = 해시, value = 참가자 이름
        sumHash += hash(p)     # 해시의 합을 구한다.

    for c in completion:
        sumHash -= hash(c)     # 완주자의 해시를 뺀다.

    return hashDict[sumHash]
