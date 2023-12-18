# 풀이 날짜 : 2023.12.18
# 문제 유형 : 스택/큐
# 문제 제목 : 프로세스
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    order = 0
    queue = [(i, priority) for i, priority in enumerate(priorities)]

    while True:
        i, priority = queue.pop(0)

        if any(priority < process[1] for process in queue):
            queue.append((i, priority))
        else:
            order += 1

            if i == location:
                return order
