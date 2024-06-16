def solution(ingredient):
    hamburger = [1,2,3,1]
    answer = 0
    stack = []
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == hamburger:
            answer +=1 
            for _ in range(4):
                stack.pop()
    return answer
