def solution(d, budget):
    answer = 0
    d = sorted(d)
    for dep in d:
        if dep > budget:
            break
        budget -= dep
        answer += 1
    return answer
