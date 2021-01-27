from math import gcd

a,b,c = map(int, input().split())

# def gcd(a,b):
#   if a < b: #a가 커야 되므로 swap
#     (a,b) = (b,a)
#   while b != 0:
#     (a,b) = (b, a%b)
#   return a

def lcm(a,b):
  return a*b//gcd(a,b)

print(lcm(a,lcm(b,c)))