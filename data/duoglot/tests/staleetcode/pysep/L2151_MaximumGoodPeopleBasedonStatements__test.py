from L2151_MaximumGoodPeopleBasedonStatements import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[[2, 1, 2], [1, 2, 2], [2, 0, 2]]]
    # output: 2
    # EXPLANATION:  Each person makes a single statement. - Person 0 states that person 1 is good. - Person 1 states that person 0 is good. - Person 2 states that person 1 is bad. Let's take person 2 as the key. - Assuming that person 2 is a good person:     - Based on the statement made by person 2, person 1 is a bad person.     - Now we know for sure that person 1 is bad and person 2 is good.     - Based on the statement made by person 1, and since person 1 is bad, they could be:         - telling the truth. There will be a contradiction in this case and this assumption is invalid.         - lying. In this case, person 0 is also a bad person and lied in their statement.     - <strong>Following that person 2 is a good person, there will be only one good person in the group</strong>. - Assuming that person 2 is a bad person:     - Based on the statement made by person 2, and since person 2 is bad, they could be:         - telling the truth. Following this scenario, person 0 and 1 are both bad as explained before.             - <strong>Following that person 2 is bad but told the truth, there will be no good persons in the group</strong>.         - lying. In this case person 1 is a good person.             - Since person 1 is a good person, person 0 is also a good person.             - <strong>Following that person 2 is bad and lied, there will be two good persons in the group</strong>. We can see that at most 2 persons are good in the best case, so we return 2. Note that there is more than one way to arrive at this conclusion.
    ,
    # example 2
    [[[2, 0], [0, 2]]]
    # output: 1
    # EXPLANATION:  Each person makes a single statement. - Person 0 states that person 1 is bad. - Person 1 states that person 0 is bad. Let's take person 0 as the key. - Assuming that person 0 is a good person:     - Based on the statement made by person 0, person 1 is a bad person and was lying.     - <strong>Following that person 0 is a good person, there will be only one good person in the group</strong>. - Assuming that person 0 is a bad person:     - Based on the statement made by person 0, and since person 0 is bad, they could be:         - telling the truth. Following this scenario, person 0 and 1 are both bad.             - <strong>Following that person 0 is bad but told the truth, there will be no good persons in the group</strong>.         - lying. In this case person 1 is a good person.             - <strong>Following that person 0 is bad and lied, there will be only one good person in the group</strong>. We can see that at most, one person is good in the best case, so we return 1. Note that there is more than one way to arrive at this conclusion.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
