def two_sum(n, arr, target):
    # write your code here
    a1 = -1
    a2 = -1
    for i in range(n-1):
      for j in range(i+1,n):
        if arr[i] + arr[j] == target:
          if a1 == -1:
            a1 = i
            a2 = j
          
    print(a1, a2)
