def test():
  "--- test function ---"
  param =[(23, 16, 16,),(56, 95, 6,),(30, 63, 1,),(51, 89, 46,),(21, 99, 38,),(69, 63, 50,),(12, 69, 73,),(44, 52, 9,),(99, 65, 10,),(46, 58, 37,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n, x, y):
  arr =[False for i in range(n + 2)]
  if(x <= n): arr[x] = True
  if(y <= n): arr[y] = True
  result = 0
  for i in range(min(x, y), n + 1):
    if(arr[i]):
      if(i + x <= n): arr[i + x] = True
      if(i + y <= n): arr[i + y] = True
      result = result + 1
  return result
"-----------------"
test()
