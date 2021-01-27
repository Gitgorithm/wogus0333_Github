w, h, b = map(int, input().split())
print('%.2f MB' %(w*h*b/pow(2,23)))