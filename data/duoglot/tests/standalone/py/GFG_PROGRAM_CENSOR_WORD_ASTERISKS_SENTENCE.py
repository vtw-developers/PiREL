def test():
  "--- test function ---"
  param =[('IggvAXtmJ', 'kzHdEJuCaO',),('76711241128', '5',),('010', '0101001',),('HIKOn', 'XlnBwpx',),('3680369217', '017523',),('1111', '1011',),('zIi', 'ONNXygON',),('06', '54171617',),('111', '0010001011001',),('NJNnrVU', 'AGwmS',)]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(text, word):
  word_list = text.split()
  result = ''
  stars = '*' * len(word)
  count = 0
  index = 0 ;
  for i in word_list:
    if i == word: word_list[index] = stars
    index += 1
  result = ' '.join(word_list)
  return result
"-----------------"
test()
