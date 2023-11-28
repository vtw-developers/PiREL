def test():
  "--- test function ---"
  param =[
    (["hello world", "hello bob", "bob hi"], ["BOB", "HELLO", "HI"]),
    (["a b c d e", "b c d e", "e f g"], ["A", "C", "E", "F"])
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    result = f_gold(* parameters_set)
"-----------------"
def f_gold(lines, word_list):
  trwords = [[y.upper() for y in x.split(" ")] for x in lines]
  count_dict = {}
  for line_split in trwords:
    for word in line_split:
      if word in word_list:
        if word not in count_dict: 
          count_dict[word] = 0
          word_list.append(word)
        count_dict[word] += 1
  for i in range(len(word_list)):
    word = word_list[i] 
    msg = "found" if word in count_dict else "not found"
    print(i, word, msg)
  count_sum = 0 
  for word in count_dict: count_sum += count_dict[word]
  return count_sum // len(word_list)
"-----------------"
test()
