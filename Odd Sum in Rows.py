def solve(N,M,arr):
  for row in arr:
    os = 0
    for col in row:
      os += col if col%2!=0 else 0
    print(os)
