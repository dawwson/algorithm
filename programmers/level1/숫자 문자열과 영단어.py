# 풀이 날짜 : 2023.12.05
# 문제 유형 : 2018 KAKAO BLIND RECRUITMENT
# 문제 제목 : 2021 카카오 채용연계형 인턴십
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    num_dict = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9', 'zero': '0'
    }
    answer = ''
    char_sum = ''

    for c in s:
        # 숫자이면 answer에 붙인다.
        if c.isdigit():
            answer = answer + c
        # 문자이면
        else:
            # sum에 붙인 후
            char_sum = char_sum + c

            # 정의된 dict에 있으면 해당 숫자를 answer에 붙이고 sum을 초기화한다.
            if char_sum in num_dict:
                answer = answer + num_dict[char_sum]
                char_sum = ''

    return int(answer)