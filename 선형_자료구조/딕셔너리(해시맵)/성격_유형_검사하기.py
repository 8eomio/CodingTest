from collections import defaultdict
def solution(survey, choices):
    answer = ""
    result = defaultdict(int)
    for ans, choice in zip(survey, choices):
        if choice < 4:
            result[ans[0]] += 4-choice
        elif choice > 4:
            result[ans[1]] += choice-4
        else:
            continue
    print(result)
    if result["R"] < result["T"]:
        answer += "T"
    else:
        answer += "R"
    if result["C"] < result["F"]:
        answer += "F"
    else:
        answer += "C"
    if result["J"] < result["M"]:
        answer += "M"
    else:
        answer += "J"
    if result["A"] < result["N"]:
        answer += "N"
    else:
        answer += "A"
    return answer
