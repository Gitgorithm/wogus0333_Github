a = []
w,h = map(int, input().split())

for i in range(w): # w,h에 맞는 이중 리스트에 0 입력
  a.append([])
  for j in range(h):
    a[i].append(0)

n = int(input())

for i in range(n):
  l, d, x, y = map(int, input().split())
  if d == 0: # 가로
   for j in range(l):
     a[x-1][y-1+j] = 1
  else: # 세로
     for j in range(l):
      a[x-1+j][y-1] = 1

for i in range(len(a)): # 이중 리스트 출력
  for j in range(len(a[i])):
    print(a[i][j], end=' ')
  print()




# for i in range(n):
#   l, d, x, y = map(int, input().split())
#   if d == 0: # 가로
#    for j in range(l):
#      a[x-1][y-1] = 1
#      y += 1
#   else: # 세로
#      for j in range(l):
#       a[x-1][y-1] = 1 
#       x += 1