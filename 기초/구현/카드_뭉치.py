from collections import deque
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for word in goal:
        if cards1 and word == cards1[0]:
            card = cards1.popleft()
        elif cards2 and word == cards2[0]:
            card = cards2.popleft()
        else:
            return "No"
    return "Yes"
