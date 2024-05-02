from collections import deque
def solution(A, B):
    answer = 0
    listA = deque(list(A))
    listB = deque(list(B))
    while listA != listB:
        listA.rotate(1)
        answer += 1
        if answer >= len(listA):
            return -1
    return answer
