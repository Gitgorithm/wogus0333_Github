inputString = ord(input())
startString = ord('a')

while startString <= inputString:
  print(chr(startString), end=' ')
  startString += 1

# while True:
#   print(chr(startString), end=' ')
#   startString += 1
#   if inputString >= startString: 
#     continue
#   else:
#     break