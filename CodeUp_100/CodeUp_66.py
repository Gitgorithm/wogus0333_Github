number = [int(x) for x in input().split()]
for num in number:
  print("even") if num%2==0 else print("odd")