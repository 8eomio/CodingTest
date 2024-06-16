def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer
