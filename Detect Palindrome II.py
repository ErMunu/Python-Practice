n = int(input())
for i in range(n):
  m = input()
  string = input()
  dic = {}
  for s in string:
    if s in dic:
      dic[s] += 1
    else:
      dic[s] = 1
  
  possible = False
  
  count = 0
  for e in dic:
    if dic[e]%2!=0:
      count += 1
  
  if count > 1:
    print("Not Possible!")
