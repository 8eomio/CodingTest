def solution(score):
    answer = []
    for i, (eng, math) in enumerate(score):
        answer.append([(eng+math)/2, i+1])
    return [final[1] for final in sorted(answer, reverse=True)]
