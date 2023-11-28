from L1419_MinimumNumberofFrogsCroaking import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["croakcroak"]
    # output: 1
    # EXPLANATION:  One frog yelling "croak<strong>"</strong> twice.
    ,
    # example 2
    ["crcoakroak"]
    # output: 2
    # EXPLANATION:  The minimum number of frogs is two.  The first frog could yell "<strong>cr</strong>c<strong>oak</strong>roak". The second frog could yell later "cr<strong>c</strong>oak<strong>roak</strong>".
    ,
    # example 3
    ["croakcrook"]
    # output: -1
    # EXPLANATION:  The given string is an invalid combination of "croak<strong>"</strong> from different frogs.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
