def solution(arr1, arr2):
    mat = []
    col = len(arr1)
    row = len(arr1[0])
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(arr1[i][j] + arr2[i][j])
        mat.append(temp)
    return mat
