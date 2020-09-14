matrix = [[1]]


def transpose(mat):
    rows_cnt = len(mat)
    cols_cnt = len(mat[0])
    new_matrix = [[0] * rows_cnt for _ in range(cols_cnt)]
    for i in range(rows_cnt):
        for j in range(cols_cnt):
            new_matrix[i][j] = mat[j][i]
    return new_matrix


matrix = transpose(matrix)
for line in matrix:
    print(*line)
