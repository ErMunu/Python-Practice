n = int(input())

while n > 0:
  l = int(input())
  arr = list(map(int,input().split(' ')))
  m = min(arr)
  res = ["-1" if num == m else str(num) for num in arr]
  print(" ".join(res))
  
  n -= 1
