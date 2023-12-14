# 풀이 날짜 : 2023.12.14
# 문제 유형 : Summer/Winter Coding(~2018)
# 문제 제목 : 영어 끝말잇기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    turns = dict.fromkeys([i for i in range(n)], 0)
    used = []

    for index, word in enumerate(words):
        turns[index % n] += 1

        # 이미 나온 단어를 말하면 탈락
        if used.count(word) != 0:
            return [index % n + 1, turns[index % n]]
        # 끝말잇기가 안 되면 탈락
        if len(used) != 0 and used[-1][-1] != word[0]:
            return [index % n + 1, turns[index % n]]
        used.append(word)

    return [0, 0]
