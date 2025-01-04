t = int(input())
while t > 0:
  n = int(input())
  a = list(map(int,input().split()))
  b = list(map(int,input().split()))
  count = 0
  b_count = {}
  for num in b:
    if num in b_count:
      b_count[num] += 1
    else:
      b_count[num] = 1
  
  for num in a:
    if num in b_count and b_count[num] > 0:
      count += 1
      b_count[num] -= 1
  print(count)
  t -= 1
