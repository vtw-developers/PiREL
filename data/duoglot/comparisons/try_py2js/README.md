# Evaluating py2js

## Entering the evaluation environment for py2js 

First run the following command inside the folder `<RepoRoot>/docker/thirdparty/` to start `duoglotcompare` container and obtain a bash shell inside the container:

```sh
./cli-duoglotcompare.sh
```

Then run the following on the container's shell to enter the `py39` conda environment where py2js is already installed:

```
cd /workspace/data/duoglot/comparisons/try_py2js/
conda activate py27
```

Then run command `python2 /root/py2js/pyjs.py -h` to check if py2js is working:
```
(py27) python2 /root/py2js/pyjs.py -h
Usage: pyjs.py [options] filename

Python to JavaScript compiler.

Options:
  -h, --help          show this help message and exit
  --output=OUTPUT     write output to OUTPUT
  --include-builtins  include py-builtins.js library in the output
```

## Evaluate py2js on GFG benchmarks

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_gfg.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_py2js_original.py trans >eval_py2js_original.trans.out.log 2>eval_py2js_original.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_py2js_original.trans.out.log | grep TRANSTIME > eval_py2js_original.trans.time.log
  cat eval_py2js_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness
  ```sh
  python3 eval_py2js_original.py fill
  python3 eval_py2js_original.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_py2js_original.py stat showerr > ./eval_py2js_original.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./standalone
  chmod 777 ./eval*.log
  ```

### **Where to get results?**

- Where to get correct rate and list of failed benchmarks?  
  Open `eval_py2js_original.stat.log` and scroll to the bottom. You should be able to see this (The number might have minor differences due to different versions of python or node installed):
  ```log
  ...
  SHOWERR: GFG_WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3.py
  SHOWERR: GFG_WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN.py
  SHOWERR: GFG_WRITE_A_C_PROGRAM_TO_CALCULATE_POWXN_1.py
  Write file: ./eval_py2js_solved_set.json
  ratio: 0.21233859397417504  skipcount: 0  executor_err_count: 2  test_err_count: 549
  ```
  - `ratio` is the correct rate. `0.212` means 21.2% of the translation pass the tests.
  - Lines start with `SHOWERR` are the failed benchmarks. 

- Where to get timing?  
  Open `eval_py2js_original.trans.time.log`. The timing of each benchmark is shown at the end of the line:
  ```log
  (GFG_ADD_1_TO_A_GIVEN_NUMBER.py) TRANSTIME:0.06526931561529636
  (GFG_ADD_1_TO_A_GIVEN_NUMBER_1.py) TRANSTIME:0.06520946230739355
  (GFG_ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS.py) TRANSTIME:0.06554968748241663
  (GFG_ALTERNATIVE_SORTING.py) TRANSTIME:0.06587361637502909
  (GFG_ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS.py) TRANSTIME:0.06516920123249292
  ...
  ```
  To get the average timing, please run the second command in the step 2 above.

- Where to check intermediate logs and results for debugging?
  - translator's `stdout`: `eval_py2js_original.trans.out.log`
  - translator's `stderr`: `eval_py2js_original.trans.err.log`
  - Python code to be translated: `./standalone/pygold/GFG*.py`
  - Translated JavaScript (raw): `./standalone/pygold/GFG*.js`
  - Translated JavaScript wrapped for testing: `./standalone/combined/GFG*.js`
  - Test output of translated JavaScript: `./standalone/output/GFG*.js.err` and `./standalone/output/GFG*.js.out`


## Evaluate py2js on Case Study 1 - LeetCode

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_leetcode.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_py2js_main.py trans >eval_py2js_main.trans.out.log 2>eval_py2js_main.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_py2js_main.trans.out.log | grep TRANSTIME > eval_py2js_main.trans.time.log
  cat eval_py2js_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness
  ```sh
  python3 eval_py2js_main.py fill
  python3 eval_py2js_main.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_py2js_main.py showerr stat > ./eval_py2js_main.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./staleetcode/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_py2js_original.*.log`, looking at `eval_py2js_main.*.log` to see the results for `LeetCode`. 
- **Note that the following correct rate `0.0` it is expected** due to py2js not capable of handling newer Python language features such as type annotations:
  ```
  ratio: 0.0  skipcount: 0  executor_err_count: 0  test_err_count: 1067
  ```
- Instead of looking into the folder `standalone` for detailed output, looking into the `staleetcode` folder.

## Evaluate py2js on Case Study 2 - CtCI

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_ctci.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_py2js_ctci.py trans >eval_py2js_ctci.trans.out.log 2>eval_py2js_ctci.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_py2js_ctci.trans.out.log | grep TRANSTIME > eval_py2js_ctci.trans.time.log
  cat eval_py2js_ctci.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness
  ```sh
  python3 eval_py2js_ctci.py fill
  python3 eval_py2js_ctci.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_py2js_ctci.py showerr stat > ./eval_py2js_ctci.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./stactci/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_py2js_original.*.log`, looking at `eval_py2js_ctci.*.log` to see the results for `LeetCode`.
- **Note that the automatically computed correct rate is wrong**, because `CtCI` programs' tests are mixed with the code being tested, and py2js is translating all the test code wrongly and none of the tests are execucted. The reported correct rate `0.84` is because that the translated code is skipping all the tests:
  ```
  SHOWERR: AL054_p02_robot_grid.py
  SHOWERR: AL072_p06_animal_shelter.py
  SHOWERR: AL114_p05_validate_bst.py
  SHOWERR: AL123_p09_bst_sequences.py
  Write file: ./eval_py2js_solved_set.json
  ratio: 0.84  skipcount: 0  executor_err_count: 0  test_err_count: 4
  ```
  After our manual validation, the actural correct rate is `0.0`, and all the files in `./stactci/output/*.js.out` are empty.
- Instead of looking into the folder `standalone` for detailed output, looking into the `stactci` folder.