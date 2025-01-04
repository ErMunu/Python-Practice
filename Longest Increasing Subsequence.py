n = int(input())
while n > 0:
  l = int(input())
  arr = list(map(int,input().split()))
  
  lis = []
  
  def bs(arr,left,right,key):
    while left < right:
      mid = (left+right)// 2
      if arr[mid] < key:
        left = mid + 1
      else:
        right = mid
    return left
  
  for num in arr:
    pos = bs(lis,0,len(lis),num)
    if pos == len(lis):
      lis.append(num)
    else:
      lis[pos] = num
  print(len(lis))
  n -= 1
