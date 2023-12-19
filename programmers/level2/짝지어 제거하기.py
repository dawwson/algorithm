# 풀이 날짜 : 2023.12.19
# 문제 유형 : 2017 팁스다운
# 문제 제목 : 짝지어 제거하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    arr = []

    for ch in s:
        if len(arr) == 0:
            arr.append(ch)
        else:
            if ch == arr[-1]:
                arr.pop()
            else:
                arr.append(ch)

    return 1 if not arr else 0
