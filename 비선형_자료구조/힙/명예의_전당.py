import heapq
def solution(k, score):
    answer = []
    kscore = []
    heapq.heapify(kscore)
    for day in score:
        heapq.heappush(kscore, day)
        if len(kscore) > k:
            heapq.heappop(kscore)
        answer.append(min(kscore))
        
    return answer
