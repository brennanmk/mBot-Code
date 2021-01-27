from numbers import Number

i = None


i = 0
for count in range(10):
  i = (i if isinstance(i, Number) else 0) + 1
  print(i)
