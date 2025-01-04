n = int(input())
s = input()
dic = {}
maxx = s[0]
for i in s:
  if i in dic:
    dic[i] += 1
    if dic[i] > dic[maxx]:
      maxx = i
  else:
    dic[i] = 1
print(maxx)
