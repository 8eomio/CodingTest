from collections import deque
def solution(numbers, direction):
    answer = []
    numbers = deque(numbers)
    if direction == "right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
