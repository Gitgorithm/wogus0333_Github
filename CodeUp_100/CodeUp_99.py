x, y = 1, 1
a = []
for i in range(10): # 이중 리스트 입력
  a.append([int(x) for x in input().split()])

for i in range(1, 20):
  if a[x][y] == 2: # 먹이 o
    a[x][y] = 9
    break
  elif a[x][y] == 0: # 먹이 x
    a[x][y] = 9
    if a[x][y+1] in (0,2): # 오른쪽 이동 가능
      y += 1
    else: # 오른쪽으로 이동 불가능
      if a[x+1][y] in (0,2): # 아래로 이동 가능
        x += 1
      else: # 아래로 이동 불가능
        break

for i in range(len(a)): # 이중 리스트 출력
  for j in range(len(a[i])):
    print(a[i][j], end=' ')
  print()