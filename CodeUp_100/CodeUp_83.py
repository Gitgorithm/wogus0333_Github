n = int(input())
for i in range(1,n+1):
  print('X', end=' ') if i%3==0 else print(i, end=' ')