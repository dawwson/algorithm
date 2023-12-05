# 풀이 날짜 : 2023.12.05
# 문제 유형 : 2018 KAKAO BLIND RECRUITMENT
# 문제 제목 : 비밀지도
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        decrypted = ''

        bin_format = '0' + str(n) +'b'  # 0b를 떼고 앞에 0을 붙여서 n자리로 맞춘다
        result = format(arr1[i] | arr2[i], bin_format)
        print(bin_format)

        for j in range(n):
            if result[j] == '1':
                decrypted = decrypted + '#'
            else:
                decrypted = decrypted + ' '

        answer.append(decrypted)
    return answer