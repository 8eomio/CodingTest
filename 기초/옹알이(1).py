import re 
def solution(babbling):
    answer = 0
    temp = ["aya", "ye", "woo", "ma"]
    for b in babbling:
        string = re.split(r"aya|ye|woo|ma", b)
        answer += 1
        for s in string:
            if s:
                answer -= 1
                break
    return answer
