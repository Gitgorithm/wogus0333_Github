from sys import stdin

n = int(stdin.readline())
number = [] # 입력 원소 
for i in range(n):
  number.append(int(stdin.readline()))

stack = [] #스택
result = [] #결과 +, -
maxNum = 1 # 현재 1부터 입력된 수열까지의 값 중 최댓값
for i in number:
  while maxNum <= i: # 1부터 입력된 수열까지
    stack.append(maxNum) # 스택에 1~i까지 push
    result.append('+') # 결과에 '+' push
    maxNum += 1
  if stack.pop() == i: # 스택 마지막 수와 입력된 수열이 같다면 pop
    result.append('-') # 결과에 '-' push
  else: # 스택 마지막 수와 입력된 수열이 다르다면 스택을 비운 후 'NO'만 push
    result.clear()
    result.append('NO')
    break # 이후 진행하지 않고 루프 탈출

for i in result: # 결과 출력
  print(i)

# n = int(input())
# number = [] # 입력 원소 
# for i in range(n):
#   number.append(int(input()))

# stack = [] #스택
# result = [] #결과 +, -
# maxNum = 1 # 현재 1부터 입력된 수열까지의 값 중 최댓값
# for i in number:
#   while maxNum <= i: # 1부터 입력된 수열까지
#     stack.append(maxNum) # 스택에 1~i까지 push
#     result.append('+') # 결과에 '+' push
#     maxNum += 1
#   if stack.pop() == i: # 스택 마지막 수와 입력된 수열이 같다면 pop
#     result.append('-') # 결과에 '-' push
#   else: # 스택 마지막 수와 입력된 수열이 다르다면 스택을 비운 후 'NO'만 push
#     result.clear()
#     result.append('NO')
#     break # 이후 진행하지 않고 루프 탈출

# for i in result: # 결과 출력
#   print(i)