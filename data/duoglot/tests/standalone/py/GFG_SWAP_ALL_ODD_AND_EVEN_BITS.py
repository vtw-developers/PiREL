def test():
  "--- test function ---"
  param =[(99,),(94,),(11,),(3,),(77,),(57,),(54,),(66,),(98,),(36,)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(x):
  even_bits = x & 0xAAAAAAAA
  odd_bits = x & 0x55555555
  even_bits >>= 1
  odd_bits <<= 1
  return(even_bits | odd_bits)
"-----------------"
test()
