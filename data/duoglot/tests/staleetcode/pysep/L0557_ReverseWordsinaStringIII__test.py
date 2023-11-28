from L0557_ReverseWordsinaStringIII import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["Let's take LeetCode contest"]
    # output: "s'teL ekat edoCteeL tsetnoc"
    ,
    # example 2
    ["God Ding"]
    # output: "doG gniD"
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
