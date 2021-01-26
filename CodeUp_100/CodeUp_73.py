#string으로 풀어보기
a = input().split()
i = 0
while i < len(a):
  if a[i] != '0':
    print(a[i])
    i += 1
  else:
    break