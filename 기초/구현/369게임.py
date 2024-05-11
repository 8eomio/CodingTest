def solution(order):
    answer = 0
    for tsn in str(order):
        if tsn in ["3", "6", "9"]:
            answer += 1
    return answer
