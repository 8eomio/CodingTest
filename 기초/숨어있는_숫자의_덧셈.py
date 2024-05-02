import re
def solution(my_string):
    answer = 0
    for string in re.split(r'[A-Za-z]', my_string):
        if string:
            answer += int(string)


    return answer
