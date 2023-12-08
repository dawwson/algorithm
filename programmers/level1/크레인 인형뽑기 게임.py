# 풀이 날짜 : 2023.12.08
# 문제 유형 : 2019 카카오 개발자 겨울 인턴십
# 문제 제목 : 크레인 인형뽑기 게임
# 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    # 터트려서 사라진 인형의 개수
    count = 0
    # 바구니
    basket = []

    for move in moves:
        for row in range(len(board)):
            pick = board[row][move-1]

            if pick != 0:
                if len(basket) != 0 and basket[-1] == pick:
                    basket.pop()
                    count += 2
                else:
                    basket.append(pick)
                board[row][move-1] = 0
                break

    return count
