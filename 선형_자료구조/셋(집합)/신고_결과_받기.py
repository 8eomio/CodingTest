from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    ban = [0] * len(id_list)
    ids = defaultdict(set)
    banned_id = []
    for i in id_list:
        ids[i] = set()
    report_id = [0] * len(id_list)
    for r in report:
        r1, r2 = r.split()
        ids[r1].add(r2)
    for bid in ids.values():
        for b in bid:
            ban[id_list.index(b)] += 1
    for i, bid in enumerate(ban):
        if bid >= k:
            banned_id.append(id_list[i])  
    for bid in banned_id:
        for i, uid in enumerate(ids.values()):
            if bid in uid:
                answer[i] += 1
            
    
    return answer
