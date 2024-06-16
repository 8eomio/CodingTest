def solution(s):
    answer = True
    stack = []
    if s[0] == ")":
        return False
    for p in s[::-1]:
        if p == "(":
            if not stack:
                return False
            else:
                stack.pop()
        else:
            stack.append(p)

    return answer
