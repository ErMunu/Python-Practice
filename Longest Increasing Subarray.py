def longest_increasing_subarray(n, arr):
    if not arr:
      print(0)
      return
    
    longest = 1
    sub_array_count = 1
    
    for i in range(n-1):
      if arr[i] < arr[i+1]:
        sub_array_count += 1
        if longest < sub_array_count:
          longest = sub_array_count
      else:
        sub_array_count = 1
    
    print(longest)
