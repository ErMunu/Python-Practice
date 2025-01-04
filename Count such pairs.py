def count_pairs_with_sum(arr, target_sum):
  #write your code here
  count = 0
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if arr[i]+arr[j] == target_sum and i != j:
        count += 1
  print(count)
