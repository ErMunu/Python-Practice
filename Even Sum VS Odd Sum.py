def Solve(N,arr):
  #write your code here
  even = 0
  odd = 0
  for i in range(N):
    if i%2 == 0:
      even += arr[i]
    else:
      odd += arr[i]
  
  if even > odd:
    print("Even")
  elif odd > even:
    print("Odd")
  else:
    print("Even Odd")
