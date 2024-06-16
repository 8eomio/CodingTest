from collections import Counter
def solution(X, Y):
    x = Counter(X)
    y = Counter(Y)
    common = x - (x-y)
    answer = ""
    for key, val in common.items():
        answer += key * val
    number = sorted(answer, reverse=True)
    if not number:
        return "-1"
    elif number[0] == "0":
        return "0"
    else:
        return "".join(number)
