a = []
for i in range(19): # 이중 리스트 입력
  a.append([int(x) for x in input().split()])

n = int(input())

for k in range(n):
  x, y = map(int, input().split())
  for i in range(19):
    a[i][y-1] = int(not(a[i][y-1])) # 세로 방향 0,1 전환
    a[x-1][i] = int(not(a[x-1][i])) # 가로 방향  0,1 전환

for i in range(len(a)): # 이중 리스트 출력
  for j in range(len(a[i])):
    print(a[i][j], end=' ')
  print()




#   for k in range(n):
#   x, y = map(int, input().split())
#   for i in range(19):
#     if a[i][y-1] == 0: # 세로 방향 0,1 전환
#       a[i][y-1]=1 
#     else:
#       a[i][y-1]=0

#     if a[x-1][i] == 0: # 가로 방향  0,1 전환
#       a[x-1][i]=1 
#     else:
#       a[x-1][i]=0

# for i in range(19): # 이중 리스트 출력
#   for j in range(19):
#     print(a[i][j], end=' ')
#   print()