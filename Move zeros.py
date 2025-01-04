n = int(input())

while n > 0:
  N =int(input())
  nums = list(map(int,input().split()))
  
  non_zeros = [num for num in nums if num != 0]
  zeros = [num for num in nums if num == 0]
  
  result = non_zeros + zeros
  
  print(" ".join(map(str,result)))
  
  n -= 1
