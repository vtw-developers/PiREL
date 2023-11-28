def test():
  "--- test function ---"
  param =[(63,),(72,),(28,),(35,),(6,),(70,),(20,),(8,),(8,),(35,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n):
  sum = 0
  for i in range(n): sum += i *(n - i)
  return 2 * sum
"-----------------"
test()
