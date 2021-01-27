a = []
for i in range(19):
  line = []
  for j in range(19):
    line.append(0)
  a.append(line)

n = int(input())
for i in range(n):
  x,y = map(int, input().split())
  a[x-1][y-1] = 1

for i in range(19):
  for j in range(19):
    print(a[i][j], end=' ')
  print()
