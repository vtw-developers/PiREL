from L0488_ZumaGame import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["WRRBBW", "RB"]
    # output: -1
    # EXPLANATION:  It is impossible to clear all the balls. The best you can do is: - Insert 'R' so the board becomes WRR<u>R</u>BBW. W<u>RRR</u>BBW -> WBBW. - Insert 'B' so the board becomes WBB<u>B</u>W. W<u>BBB</u>W -> WW. There are still balls remaining on the board, and you are out of balls to insert.
    ,
    # example 2
    ["WWRRBBWW", "WRBRW"]
    # output: 2
    # EXPLANATION:  To make the board empty: - Insert 'R' so the board becomes WWRR<u>R</u>BBWW. WW<u>RRR</u>BBWW -> WWBBWW. - Insert 'B' so the board becomes WWBB<u>B</u>WW. WW<u>BBB</u>WW -> <u>WWWW</u> -> empty. 2 balls from your hand were needed to clear the board.
    ,
    # example 3
    ["G", "GGGGG"]
    # output: 2
    # EXPLANATION:  To make the board empty: - Insert 'G' so the board becomes G<u>G</u>. - Insert 'G' so the board becomes GG<u>G</u>. <u>GGG</u> -> empty. 2 balls from your hand were needed to clear the board.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
