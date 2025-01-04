n = int(input())
s = input()
m = int(input())

check = True
while check:
  dic = {}
  for i in s:
    if i in dic:
      dic[i] += 1
    else:
      dic[i] = 1
  chk = True
  for i in dic.values():
    if i < m:
      chk = False
  
  if not chk:
    s = s[0:-1]
  else:
    check = False
    print(len(s))
      
