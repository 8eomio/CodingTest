from collections import defaultdict
def solution(score):
    ranks = defaultdict(list)
    for idx, student in enumerate(score):
        ranks[sum(student)].append(idx)
    result = [0 for _ in range(len(score))]
    rank = 1

    for _, indices in sorted(ranks.items(), reverse=True):
        for index in indices:
            result[index] = rank
        rank += len(indices)
    return result
