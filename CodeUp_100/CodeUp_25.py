while True:
  a = input()
  if int(a) < 10000 & int(a) > 99999: # a 범위가 아니면
    continue
  for i in range(len(a)):
    print("[" + a[i] + "0"*(4-i) + "]")
  break
