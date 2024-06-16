
def solution(array, n):
    return sorted(array , key= lambda x: (abs(n-x),x))[0]
