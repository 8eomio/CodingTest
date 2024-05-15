def solution(answers):
    student1 = [1,2,3,4,5] 
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    scores = [0,0,0]

    for idx, ans in enumerate(answers):
        if student1[idx % len(student1)] == answers[idx]:
            scores[0] += 1
        if student2[idx % len(student2)] == answers[idx]:
            scores[1] += 1
        if student3[idx % len(student3)] == answers[idx]:
            scores[2] += 1
    answer = []
    max_num = max(scores)
    for i, ans in enumerate(scores):
        if ans == max_num:
            answer.append(i+1)
    return answer
