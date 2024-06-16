from string import ascii_lowercase
def solution(s, skip, index):
    a_to_z = set(ascii_lowercase)
    a_to_z -= set(skip)
    a_to_z = sorted(a_to_z)
    
    dic_alpha = {alpha: idx for idx, alpha in enumerate(a_to_z)}
    
    result = ""
    for i in s:
        result += a_to_z[(dic_alpha[i]+index)%len(a_to_z)]
    return result
