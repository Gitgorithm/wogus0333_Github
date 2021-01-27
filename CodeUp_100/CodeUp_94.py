n = input()
number = list(map(int, input().split()))
number.reverse()

for i in number:
  print(i, end=' ')

# for i in reversed(number):
#   print(i, end=' ')