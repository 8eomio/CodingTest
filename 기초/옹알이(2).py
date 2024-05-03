def solution(babbling):
    answer = 0
    sound = ["aya", "ye", "woo", "ma"]
    sound2 = [s*2 for s in sound]
    for b in babbling:
        for i, s in enumerate(sound):
            if sound2[i] in b:
                continue
            else:
                b=b.replace(s, " ")
        if len(b.strip()) == 0:
            answer += 1
    return answer
