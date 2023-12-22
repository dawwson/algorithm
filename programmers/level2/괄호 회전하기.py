# 풀이 날짜 : 2023.12.22
# 문제 유형 : 월간 코드 챌린지 시즌2
# 문제 제목 : 괄호 회전하기
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    x_count = 0

    for x in range(len(s)):
        rotated = s[x:] + s[0:x]
        stack = []

        for i in range(len(rotated)):
            if len(stack) == 0:
                stack.append(rotated[i])
            elif stack[-1] == '[' and rotated[i] == ']' or stack[-1] == '{' and rotated[i] == '}' or stack[-1] == '(' and rotated[i] == ')':
                stack.pop()
            else:
                stack.append(rotated[i])

        if len(stack) == 0:
            x_count += 1

    return x_count
