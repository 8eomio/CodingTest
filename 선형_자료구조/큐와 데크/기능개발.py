from collections import deque
def solution(progresses, speeds):
    answer = []
    days = deque()
    for i, p in enumerate(progresses):
        if (100-p) % speeds[i]: 
            days.append(((100-p) // speeds[i]) + 1)
        else:
            days.append(((100-p) // speeds[i]))
    print(days)
    temp = 1
    temp_day = days.popleft()
    while days:
        day = days.popleft()
        if day <= temp_day:
            temp += 1
        else:
            answer.append(temp)
            temp=1
            temp_day = day
    answer.append(temp)
    return answer
