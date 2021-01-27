n = input()
number = [int(x) for x in input().split()]
result = [0]*23
# for i in range(24) :
#     arr.append(0)

for i in number:
  result[i-1] += 1

for count in result:
  print(count, end=' ')