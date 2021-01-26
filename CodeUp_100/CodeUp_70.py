month = int(input())
season = {(12,1,2):'winter', (3,4,5):'spring', (6,7,8):'summer', (9,10,11):'fall'}
for key in season.keys():
  if month in key: print(season[key])

#key 값 : tuple O / list X

# if month in [12,1,2]:
#   print('winter')
# elif month in [3,4,5]:
#   print('spring')
# elif month in [6,7,8]:
#   print('summer')
# elif month in [9,10,11]:
#   print('fall')

# in 뒤에 tuple O / list O