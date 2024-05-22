def solution(my_string):
    answer = ""
    for string in my_string:
        if string in answer:
            continue
        else:
            answer += string
    return answer
