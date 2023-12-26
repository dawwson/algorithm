# 풀이 날짜 : 2023.12.26
# 문제 유형 : 월간 코드 챌린지 시즌3
# 문제 제목 : n^2 배열 자르기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/131127


def solution(n, left, right):
    answer = []

    # 2차원 배열에서 좌표[x,y]의 값은 max(x+1,y+1)
    # (0,0) (0,1) (0,2)
    # (1,0) (1,1) (1,2)
    # (2,0) (2,1) (2,2)

    # 1차원 배열에서 좌표값은 max((인덱스//n)+1, (인덱스%n)+1)
    # (0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)

    for i in range(left, right + 1):
        answer.append(max(i // n + 1, i % n + 1))

    return answer


# 시간 초과
# def solution(n, left, right):
#     arr = [[0 for _ in range(n)] for _ in range(n)]
#     answer = []

#     for i in range(0, n):
#         # 대각선을 채운다.
#         arr[i][i] = i + 1

#         # 행 이동하여 채우기
#         for row in range(i, -1, -1):
#             arr[row][i] = i + 1
#         # 열 이동하여 채우기
#         for col in range(i, -1, -1):
#             arr[i][col] = i + 1

#     # 잘라서 이어붙이기
#     joined = [element for row in arr for element in row]

#     return joined[left:right+1]
