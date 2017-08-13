def zeroMatrix(matrix):
    target = []
    for i in range(len(matrix)):
        for j in matrix[i]:
            if j == 0:
                target.append(i)

    for row in target:
        size = len(matrix[row])
        matrix[row] = [0] * size
    return matrix

_m = [
    [1,2,3,4,5,6,7,8],
    [4,5,7,6,8,4,2,5],
    [1,2,6,4,7,0,7,4],
    [4,5,7,2,5,8,9,3],
    [4,0,4,5,7,8,2,3]
]

print(_m)
print(zeroMatrix(_m))
