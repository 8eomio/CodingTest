def solution(chicken):
    answer = 0
    while chicken >= 10 :
        free = chicken //10
        answer += free
        chicken += free - free*10
    return answer
