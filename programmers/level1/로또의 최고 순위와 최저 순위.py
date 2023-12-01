def solution(lottos, win_nums):
    rank_dict = {
        6: 1,
        5: 2,
        4: 3,
        3: 4,
        2: 5,
        1: 6,
        0: 6
    }
    matched = 0
    unknown = 0

    for index, lotto in enumerate(lottos):
        if lotto in win_nums:
            matched += 1
        elif lotto == 0:
            unknown += 1

    highest_rank = rank_dict[matched + unknown]
    lowest_rank = rank_dict[matched]

    return [highest_rank, lowest_rank]
