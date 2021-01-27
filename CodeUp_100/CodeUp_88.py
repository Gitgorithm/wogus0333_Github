inputNumber = int(input())

for i in range(1,inputNumber+1):
  if not(i%3==0):
    print(i, end=' ')

# not(i%3==0) == i%3!=0


# for i in range(1, n+1) :
#     if i%3==0 :
#         continue
#     print(i, end=' ')