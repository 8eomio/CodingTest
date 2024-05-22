from collections import defaultdict
def solution(array):
    answer = 0
    num_dict = defaultdict(int)
    for num in array:
        num_dict[num] += 1
    num_dict = sorted(num_dict.items(), key = lambda item: item[1], reverse=True)
    if len(num_dict) > 1 and num_dict[0][1] == num_dict[1][1]:
        return -1
    else:
        return num_dict[0][0]
