def solution(num, total):
    init_num = (total - (num*(num-1) / 2)) / num 
    return [i for i in range(int(init_num), int(init_num + num))]
