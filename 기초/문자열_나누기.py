def solution(s):
    answer = 0
    same = 1
    diff = 0
    x = s[0]
    for string in s[1:]:
        if same == diff:
            answer += 1
            x = string
            same = 1
            diff = 0
            continue
        if string != x:
            diff += 1
        elif string == x:
            same += 1   
    return answer + 1
