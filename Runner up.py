n = int(input())

while n > 0:
  m = input()
  nums = list(map(int,input().split()))
  
  print(sorted(nums)[-2])
  
  n -= 1
