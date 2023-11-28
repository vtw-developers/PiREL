from L1994_TheNumberofGoodSubsets import f_gold

##########
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    [[1, 2, 3, 4]]
    # output: 6
    # EXPLANATION:  The good subsets are: - [1,2]: product is 2, which is the product of distinct prime 2. - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3. - [1,3]: product is 3, which is the product of distinct prime 3. - [2]: product is 2, which is the product of distinct prime 2. - [2,3]: product is 6, which is the product of distinct primes 2 and 3. - [3]: product is 3, which is the product of distinct prime 3.
    ,
    # example 2
    [[4, 2, 3, 15]]
    # output: 5
    # EXPLANATION:  The good subsets are: - [2]: product is 2, which is the product of distinct prime 2. - [2,3]: product is 6, which is the product of distinct primes 2 and 3. - [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5. - [3]: product is 3, which is the product of distinct prime 3. - [15]: product is 15, which is the product of distinct primes 3 and 5.
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)

##########

test()
