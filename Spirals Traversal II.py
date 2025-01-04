def spiral_traversal(matrix, N):
  #write your code here
  result=[]
  rows,cols = N,N
  top, bottom, left, right = 0, rows-1, 0, cols-1
  
  while top <= bottom and left <= right:
    for col in range(left,right+1):
      result.append(matrix[bottom][col])
    bottom -= 1
    
    for row in range(bottom,top-1,-1):
      result.append(matrix[row][right])
    right-=1
    
    if top <= bottom:
      for col in range(right, left-1,-1):
        result.append(matrix[top][col])
      top += 1
    
    if left <=right:
      for row in range(top,bottom+1):
        result.append(matrix[row][left])
      left+=1
  
  print(" ".join(map(str,result)))
