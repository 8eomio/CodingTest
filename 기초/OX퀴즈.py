def solution(quiz):
    answer = []
    for q in quiz:
        eq = q.split(sep = "=")
        if eval(eq[0]) == int(eq[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer
