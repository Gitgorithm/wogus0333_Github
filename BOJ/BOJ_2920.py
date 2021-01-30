a = [int(x) for x in input().split()]
result = "ascending"
for i in range(len(a)-1):
  if a[i+1]-a[i] == 1: # 오름차순
    result = "ascending"
  elif a[i+1]-a[i] == -1: # 내림차순
    result = "descending"
  else: # 혼합
    result = "mixed"
    break # 한 번이라도 혼합이면 루프 탈출
print(result)