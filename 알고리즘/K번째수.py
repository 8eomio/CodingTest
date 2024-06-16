def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        find = command[2]-1
        target_arr = array[start:end]
        target_arr.sort()
        answer.append(target_arr[find])
  
    return answer
