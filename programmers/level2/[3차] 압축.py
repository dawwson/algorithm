# 풀이 날짜 : 2024.01.05
# 문제 유형 : 2018 KAKAO BLIND RECRUITMENT
# 문제 제목 : [3차] 압축
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    # { 'A': 1, 'B': 2, ...}
    words = {chr(i+64): i for i in range(1, 27)}
    last = 27
    answer = []

    while True:
        if msg in words:
            answer.append(words[msg])
            break

        for i in range(1, len(msg)+1):
            # 사전에 없으면
            if msg[:i] not in words:
                # 색인 번호 출력(그 앞 글자까지만)
                answer.append(words[msg[:i-1]])

                # 사전에 등록
                words[msg[:i]] = last
                last += 1

                # 입력값 수정
                msg = msg[i-1:]
                break

    return answer
