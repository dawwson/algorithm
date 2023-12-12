# 풀이 날짜 : 2023.12.12
# 문제 유형 : 2023 KAKAO BLIND RECRUITMENT
# 문제 제목 : 개인정보 수집 유효기간
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    deleted = []

    today_year, today_month, today_day = map(int, today.split('.'))
    # 일수로 환산
    today_count = (today_year * 12 * 28) + (today_month * 28) + today_day
    # {'A': 1, 'B': 2, ...}
    terms_dict = {key: int(value) for key, value in (term.split() for term in terms)}

    for index, privacy in enumerate(privacies):
        date, term_type = privacy.split()
        # 수집일
        year, month, day = map(int, date.split('.'))
        # 유효기간(n개월)
        term_period = terms_dict[term_type]
        # 일수로 환산
        date_count = (year * 12 * 28) + (month * 28) + day

        if (today_count - date_count) / 28 >= term_period:
            deleted.append(index)

    return list(map(lambda i: i + 1, deleted))
