def win(hand):
    if hand == "2":
        return "0"
    elif hand == "0":
        return "5"
    elif hand == "5":
        return "2"
def solution(rsp):
    answer = ''
    for hand in rsp:
        answer += win(hand)
    return answer
