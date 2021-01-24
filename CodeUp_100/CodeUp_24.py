while True:
  a = input()
  if len(a) > 20: # 단, 단어의 길이는 20자 이하
    continue
  for i in range(len(a)):
    print("'" + a[i] + "'")
  break
