def test():
  "--- test function ---"
  param =[(83,),(88,),(60,),(6,),(26,),(98,),(38,),(90,),(76,),(66,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(num):
  sum = 0
  i = 2
  while(i * i <= num):
    while(num % i == 0):
      sum += i
      num /= i
    i += 1
  sum += num
  return sum
"-----------------"
test()
