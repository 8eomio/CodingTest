from collections import defaultdict

def solution(clothes):
    fashion = defaultdict(list)
    answer = 1
    for cloth in clothes:
        fashion[cloth[1]].append(cloth[0])
    
    for cloth_key in fashion.keys():
        answer += answer * len(fashion[cloth_key])
        
    return answer-1
