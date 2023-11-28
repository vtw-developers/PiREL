from L0388_LongestAbsoluteFilePath import f_gold

##########
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

##########

test()
