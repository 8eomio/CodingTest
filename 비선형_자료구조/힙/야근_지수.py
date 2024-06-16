import heapq
def solution(n, works):
    if sum(works) < n:
        return 0
    answer = 0
    works = [-work for work in works]
    heapq.heapify(works)
    for hour in range(n):
        work = heapq.heappop(works)
        if work + 1 == 0:
            continue
        heapq.heappush(works, work + 1)
    return sum([done**2 for done in works])
