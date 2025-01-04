def Solve(N,M,matrix):
  #write your code here
  for i in range(M):
    product = 1
    for j in range(N):
      if matrix[j][i] % 2 == 0:
        product *= matrix[j][i]
    print(product)
