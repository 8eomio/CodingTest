def solution(lottos, win_nums):
    min_score = 0
    for lotto in lottos:
        if lotto in win_nums:
            min_score += 1
            win_nums.pop(win_nums.index(lotto))
    max_score = min(lottos.count(0), len(win_nums)) + min_score

    return [min(7 - max_score,6), min(7 - min_score, 6)]
