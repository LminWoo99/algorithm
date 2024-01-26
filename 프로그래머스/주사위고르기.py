from itertools import combinations, product
import bisect


def solution(dice):
    answer = []
    max_win_count = 0

    dice_set = {i for i in range(len(dice))}
    for a_choice in combinations([i for i in range(len(dice))], len(dice) // 2):
        a_sum_list = make_sum_list(a_choice, dice)
        b_choice = list(dice_set.difference(a_choice))
        b_sum_list = make_sum_list(b_choice, dice)

        win_count = 0
        for i in range(len(a_sum_list)):
            win_count += bisect.bisect_left(b_sum_list, a_sum_list[i])

        if win_count > max_win_count:
            max_win_count = win_count
            answer = sorted(list(a_choice))

    return [i + 1 for i in answer]


def make_sum_list(choice, dice):
    # choice [1,2,3,4,5]
    sum_list = []
    for pr in product([i for i in range(6)], repeat=len(choice)):  # 각 주사위의 idx 순열
        sum = 0
        for select_dice, idx in zip(choice, pr):
            sum += dice[select_dice][idx]
        sum_list.append(sum)

    return sorted(sum_list)
solution([[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]])