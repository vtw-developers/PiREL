def test():
  "--- test function ---"
  param =[('m Dm YZ',),('65 48 57 71',),('01 010',),('mT vhByi',),('19 44 9 1',),('0',),('z vUi  ',),('7 591 36643 9 055',),('01',),('ti YGaijPY',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(str):
  i = len(str)- 1
  start = end = i + 1
  result = ''
  while i >= 0:
    if str[i] == ' ':
      start = i + 1
      while start != end:
        result += str[start]
        start += 1
      result += ' '
      end = i
    i -= 1
  start = 0
  while start != end:
    result += str[start]
    start += 1
  return result
"-----------------"
test()
