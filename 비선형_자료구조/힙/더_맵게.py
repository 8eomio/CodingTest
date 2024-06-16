import heapq
def stir(first, second):
    return first + (second*2)
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True and len(scoville) >= 2:
        first = heapq.heappop(scoville)
        if first >= K:
            break
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, stir(first, second))
        answer += 1
    if heapq.heappop(scoville) < K:
        return -1
    else:
        return answer
