m1,n1 = input().split(" ")
sum1 = 0
for i in range(int(m1)):
  sum1 += sum(list(map(int, input().split(" "))))
  
m2,n2 = input().split(" ")
sum2 = 0
for i in range(int(m2)):
  sum2 += sum(list(map(int, input().split(" "))))
  
print(sum1 if sum1 > sum2 else sum2)
