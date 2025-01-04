n = int(input())
while n != 0:
  cars = list(map(int, input().split()))
  sidelane = []
  mainlane = []
  for car in cars:
    x = mainlane[-1]+1 if mainlane else 1
    y = sidelane[-1] if sidelane else 0
    if car == x:
      mainlane.append(car)
    elif y == x:
      mainlane.append(sidelane.pop())
    else:
      sidelane.append(car)
  while sidelane:
    mainlane.append(sidelane.pop())
  
  print('yes' if mainlane == sorted(mainlane) else 'no')
  n = int(input())
