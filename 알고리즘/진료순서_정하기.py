
def solution(emergency):
    answer = [0] * len(emergency)
    rank = [(i, e) for i, e in enumerate(emergency)]
    rank = sorted(rank, key = lambda x: x[1], reverse =True)
    for idx, (i,e) in enumerate(rank):
        answer[i] = idx+1
    return answer
