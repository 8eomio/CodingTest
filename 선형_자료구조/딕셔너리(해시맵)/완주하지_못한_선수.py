def solution(participant, completion):
    participant.sort()
    completion.sort()
    idx = 0
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            idx = i
            break
        else:
            idx = len(completion)

    return participant[idx]
