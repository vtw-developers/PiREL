from L1418_DisplayTableofFoodOrdersinaRestaurant import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[["David", "3", "Ceviche"], ["Corina", "10", "Beef Burrito"], ["David", "3", "Fried Chicken"], ["Carla", "5", "Water"], ["Carla", "5", "Ceviche"], ["Rous", "3", "Ceviche"]]]
    # output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
    # EXPLANATION: The displaying table looks like:  <strong>Table,Beef Burrito,Ceviche,Fried Chicken,Water</strong>  3    ,0           ,2      ,1            ,0  5    ,0           ,1      ,0            ,1  10   ,1           ,0      ,0            ,0  For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".  For the table 5: Carla orders "Water" and "Ceviche".  For the table 10: Corina orders "Beef Burrito".
    ,
    # example 2
    [[["James", "12", "Fried Chicken"], ["Ratesh", "12", "Fried Chicken"], ["Amadeus", "12", "Fried Chicken"], ["Adam", "1", "Canadian Waffles"], ["Brianna", "1", "Canadian Waffles"]]]
    # output: [["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
    # EXPLANATION:    For the table 1: Adam and Brianna order "Canadian Waffles".  For the table 12: James, Ratesh and Amadeus order "Fried Chicken".
    ,
    # example 3
    [[["Laura", "2", "Bean Burrito"], ["Jhon", "2", "Beef Burrito"], ["Melissa", "2", "Soda"]]]
    # output: [["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
