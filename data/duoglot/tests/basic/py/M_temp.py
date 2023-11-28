bar = True
y = [1, [21, 22], 3, 4, 5]
str_list = [str(x) for x in y]
c = " good nice";
print("hi" + str(bar))

a = 0
for i in range(10):
  for j in range(10, i, -1):
    a += abs(i * j)

def baz(x, y, z): pass

def foo(x, y):
  a = x
  z = x + y
  if bar:
    baz("hello", x, y)
    return z
  return x - y

try:
  raise Exception("CustomError")
except Exception as e:
  print("Exception!")
  print(e)