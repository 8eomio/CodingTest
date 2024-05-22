from collections import defaultdict
def solution(s):
    close = defaultdict(int)
    answer = []
    for i, letter in enumerate(s):
        answer.append(i - close.get(letter, i+1 ))
        close[letter] = i
    return answer
