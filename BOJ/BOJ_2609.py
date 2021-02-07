from math import gcd

a, b = map(int, input().split())
gcdNum = gcd(a,b)
lcmNum = a*b//(gcdNum)
print(gcdNum)
print(lcmNum)