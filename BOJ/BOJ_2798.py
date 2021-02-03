n, m = map(int, input().split())
randomNum = [int(x) for x in input().split()]
maxSum = -1
for i in range(len(randomNum)):
  for j in range(i+1,len(randomNum)):
    for k in range(j+1, len(randomNum)):
      sumTemp = randomNum[i] + randomNum[j] + randomNum[k]
      if(maxSum <= sumTemp <= m):
          maxSum = sumTemp
print(maxSum)


# while True:
#   n, m = map(int, input().split())
#   if(3 <= n <= 100 and 10 <= m <= 300000):
#     break
# randomNum = []
# maxSum = -1
# while maxSum == -1:
#   while len(randomNum) < n:
#     randomTemp = random.randint(1,m) #
#     if(randomTemp > 100000):
#       continue
#     if(randomTemp not in randomNum):
#       randomNum.append(randomTemp)

#   for i in range(len(randomNum)):
#     for j in range(i+1,len(randomNum)):
#       for k in range(j+1, len(randomNum)):
#         sumTemp = randomNum[i] + randomNum[j] + randomNum[k]
#         if(maxSum <= sumTemp <= m):
#           maxSum = sumTemp
#   if maxSum == -1:
#     randomNum.clear()

# print(maxSum)


