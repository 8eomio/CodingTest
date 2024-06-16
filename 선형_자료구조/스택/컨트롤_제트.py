def solution(s):
    stack =[]
    for char in s.split():
        if char == "Z":
            stack.pop()
        else:
            stack.append(int(char))
    return sum(stack)
