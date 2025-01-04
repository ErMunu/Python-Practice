m,n = map(int, input().strip().split())
matrix = [list(map(int, input().strip().split())) for _ in range(m)]

matrix_transpose = zip(matrix)
print(' '.join(str(min(col)) for col in matrix_transpose))
