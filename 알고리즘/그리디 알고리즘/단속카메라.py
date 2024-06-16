def solution(routes):
    answer = 0
    routes = sorted(routes, key= lambda x: x[1])
    last_camera = -30001
    for route in routes:
        if last_camera < route[0]:
            answer +=1
            last_camera = route[1]
    
    return answer
