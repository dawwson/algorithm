# 풀이 날짜 : 2023.11.29
# 문제 유형 : 해시
# 문제 제목 : 폰켓몬
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # 중복되지 않는 자료구조(set)에 넣는다.
    type_set = set(nums)
    # set에서 n/2(=> len(nums) / 2)개 선택 (무조건 짝수)
    select_count = len(nums) / 2

    if select_count >= len(type_set):
        return len(type_set)
    return select_count
