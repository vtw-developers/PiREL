def test():
  "--- test function ---"
  param =[(67,),(90,),(55,),(90,),(83,),(32,),(58,),(38,),(87,),(87,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(n): return(n % 2 == 0)
"-----------------"
test()
