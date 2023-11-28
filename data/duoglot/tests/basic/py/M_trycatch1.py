
bar = None
a = 5
b = 0
try:
  bar = a / b
  print("bar:", bar)
except ZeroDivisionError as e:
  print("division by zero!")
print("bar=", bar)