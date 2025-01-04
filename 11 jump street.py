n = int(input())

while n > 0:
  m = input()
  s = input()
  first = 0
  last = 0
  prev = -1
  for i in range(len(s)):
    if first == 0 and prev == '1' and s[i] == '0':
      first = i
    elif prev == '0' and s[i] == '1':
      last = i
    prev = s[i]
  print(last-first + (1 if first != 0 else 0))
  
  n -= 1
