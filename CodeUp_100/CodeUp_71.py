number = [int(x) for x in input().split()]
# list(map(int,input().split()))
for num in number:
  if num != 0:
    print(num)  
  else:
    break