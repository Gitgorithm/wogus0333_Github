a,b = map(int, input().split())
print(1) if a == b else print(0)
# print(int(not(a^b)))
# not을 하면 True or false로 표기되므로 int 변환 필요
# if else 문이 더 연산속도가 빠르고 문제에 최적화된 풀이라고 생각