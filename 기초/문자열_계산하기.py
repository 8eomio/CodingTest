def solution(my_string):
    my_op = my_string.split(" ")
    ans = int(my_op[0])
    flg = 0
    for op in my_op[1:]:
        if op == "+":
            flg = 0
        elif op == "-":
            flg = 1
        else:
            if flg == 0:
                ans += int(op)
            else:
                ans -= int(op)
            
    return ans
        
