from collections import Counter
def solution(before, after):
    b = Counter(before)
    a = Counter(after)
    if a == b:
        return 1
    else:
        return 0
