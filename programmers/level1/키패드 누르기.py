def solution(numbers, hand):
    answer = ''

    # 왼쪽/중간/오른쪽 키패드
    lefts = [1, 4, 7]
    middles = [2, 5, 8, 0]
    rights = [3, 6, 9]
    # 현재 왼손/오른손 위치
    current_left = '*'
    current_right = '#'

    # 중간 키패드로부터 다른 키패드까지의 이동 거리
    distance = {
        2: {1: 1, 2: 0, 3: 1, 4: 2, 5: 1, 6: 2, 7: 3, 8: 2, 9: 3, '*': 4, 0: 3, '#': 4},
        5: {1: 2, 2: 1, 3: 2, 4: 1, 5: 0, 6: 1, 7: 2, 8: 1, 9: 2, '*': 3, 0: 2, '#': 3},
        8: {1: 3, 2: 2, 3: 3, 4: 2, 5: 1, 6: 2, 7: 1, 8: 0, 9: 1, '*': 2, 0: 1, '#': 2},
        0: {1: 4, 2: 3, 3: 4, 4: 3, 5: 2, 6: 3, 7: 2, 8: 1, 9: 2, '*': 1, 0: 0, '#': 1}
    }

    for number in numbers:
        # 왼쪽 키패드인 경우
        if number in lefts:
            answer += 'L'
            current_left = number
        # 오른쪽 키패드인 경우
        if number in rights:
            answer += 'R'
            current_right = number
        # 중간 키패드인 경우
        if number in middles:
            # 키패드에서 현재 왼손/오른손까지의 이동 거리
            left_distance = distance[number][current_left]
            right_distance = distance[number][current_right]

            if left_distance < right_distance:
                answer += 'L'
                current_left = number
            if left_distance > right_distance:
                answer += 'R'
                current_right = number
            if left_distance == right_distance:
                # 왼손잡이
                if hand == 'left':
                    answer += 'L'
                    current_left = number
                # 오른손잡이
                if hand == 'right':
                    answer += 'R'
                    current_right = number
    return answer
