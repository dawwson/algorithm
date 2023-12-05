# 풀이 날짜 : 2023.11.28
# 문제 유형 : 탐욕법(Greedy)
# 문제 제목 : 체육복
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    # 여분의 체육복이 있는 학생 중 도난 당하지 않은 학생
    _reserve = [r for r in reserve if r not in lost]
    _reserve.sort()
    # 도난 당한 학생 중 여분의 체육복이 없는 학생
    _lost = [l for l in lost if l not in reserve]
    _lost.sort()

    # 빌려줄 수 있는 학생 기준으로 loop 진행
    for r in _reserve:
        # 앞 번호
        f = r - 1
        # 뒷 번호
        b = r + 1
        # 앞 번호가 도난 당한 학생이면 빌려줌
        if f in _lost:
            _lost.remove(f)
        # 뒷 번호가 도난 당한 학생이면 빌려줌
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)