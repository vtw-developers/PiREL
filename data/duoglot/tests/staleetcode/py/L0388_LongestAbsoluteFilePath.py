
# ++++++ to be replaced by tester ++++++
mylog = print
myexactlog = print
"+++++++++++++++++"

def test():
  "--- test function ---"
  param = [
    # example 1
    ["dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"]
    # output: 20
    # EXPLANATION:  We have only one file, and the absolute path is "dir/subdir2/file.ext" of length 20.
    ,
    # example 2
    ["dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"]
    # output: 32
    # EXPLANATION:  We have two files: "dir/subdir1/file1.ext" of length 21 "dir/subdir2/subsubdir2/file2.ext" of length 32. We return 32 since it is the longest absolute path to a file.
    ,
    # example 3
    ["a"]
    # output: 0
    # EXPLANATION:  We do not have any files, just a single directory named "a".
    ,
  ]
  for i, parameters_set in enumerate(param):
    idx = i
    mylog(0, idx)
    result = f_gold(* parameters_set)
    myexactlog(1, result)


"-----------------"
### lengthLongestPath 
from typing import *
def f_gold(input: str) -> int:
    i, n = 0, len(input)
    ans = 0
    stk = []
    while i < n:
        ident = 0
        while input[i] == '\t':
            ident += 1
            i += 1
        cur, isFile = 0, False
        while i < n and input[i] != '\n':
            cur += 1
            if input[i] == '.':
                isFile = True
            i += 1
        i += 1
        # popd
        while len(stk) > 0 and len(stk) > ident:
            stk.pop()
        if len(stk) > 0:
            cur += stk[-1] + 1
        # pushd
        if not isFile:
            stk.append(cur)
            continue
        ans = max(ans, cur)
    return ans
"-----------------"
test()

