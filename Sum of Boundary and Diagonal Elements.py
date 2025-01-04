def sum_boundary_and_diagonals(matrix, n):
    #write your code here
    result = 0
    for i in range(n):
      for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i == n-j-1:
          result += matrix[i][j]
          #print(i,j)
    print(result)
