def solution(n, lost, reserve):
    reserve, lost = set(reserve) - set(lost), set(lost) - set(reserve)
    for res in sorted(reserve):
        if res-1 in lost:
            lost.remove(res-1)
        elif res+1 in lost:
            lost.remove(res+1)
    return n - len(lost)
