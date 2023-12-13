# 풀이 날짜 : 2023.12.13
# 문제 유형 : 스택/큐
# 문제 제목 : 올바른 괄호
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for bracket in s:
        if len(stack) == 0:
            stack.append(bracket)
        else:
            if stack[-1] == '(' and bracket == ')':
                stack.pop()
            else:
                stack.append(bracket)

    # 스택이 비어있으면 True, 아니면 False
    return not stack
