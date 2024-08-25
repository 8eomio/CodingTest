def solution(n):
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    arr = [[0]*i for i in range(1, n+1)]
    x = y = angle = 0
    cnt = 1
    size = (n+1)*n //2 
    
    while cnt <= size:
        arr[y][x] = cnt 
        ny = y + dy[angle]
        nx = x + dx[angle]
        cnt += 1
        if 0<=ny<n and 0 <= nx<= ny and arr[ny][nx]==0:
            y = ny
            x = nx
        else:
            angle = (angle+1)%3
            y += dy[angle]
            x += dx[angle]
        
        
    answer = [i for j in arr for i in j]
    
    
    return answer
