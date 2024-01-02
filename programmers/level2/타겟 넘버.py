# 풀이 날짜 : 2024.01.02
# 문제 유형 : 깊이/너비 우선 탐색(DFS/BFS)
# 문제 제목 : 타겟 넘버
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    #                  root
    #           +4           -4     => depth 0
    #       +1        -1            => depth 1
    #   +2     -2   +2  -2          => depth 2
    # +1 -1  +1 -1                  => depth 3

    global count
    count = 0

    recursive_dfs(numbers, target, 0, 0)

    return count

def recursive_dfs(numbers, target, depth, s):
    global count

    if depth == len(numbers):
        if s == target:
            count += 1
        return

    recursive_dfs(numbers, target, depth+1, s+numbers[depth])
    recursive_dfs(numbers, target, depth+1, s-numbers[depth])
