# 풀이 날짜 : 2023.12.27
# 문제 유형 : 연습문제
# 문제 제목 : 행렬의 곱셈
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12949

def solution(arr1, arr2):
    # 1, 4  3, 3  = 3+12  3+12
    # 3, 2  3, 3    9+6   9+6
    # 4, 1          12+3  12+3

    # 2,3,2  5,4,3  = 10+6+6 8+12+2 6+3+2
    # 4,2,4  2,4,1
    # 3,1,4  3,1,1

    # arr1의 열의 수 = arr2의 행의 수
    # 결과 행렬의 크기: len(arr1) X len(arr2[0])
    # 결과의 열의 수 = arr1의 행의 수
    # 결과의 행의 수 = arr2의 열의 수

    result = []

    for i in range(len(arr1)):
        new_row = []

        for j in range(len(arr2[0])):
            sum = 0

            for k in range(len(arr1[0])):
                sum += arr1[i][k] * arr2[k][j]

            new_row.append(sum)

        result.append(new_row)

    return result
