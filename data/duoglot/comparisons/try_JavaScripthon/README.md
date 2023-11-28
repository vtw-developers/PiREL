# Evaluating JavaScripthon

## Entering the evaluation environment for JavaScripthon 

First run the following command inside the folder `<RepoRoot>/docker/thirdparty/` to start `duoglotcompare` container and obtain a bash shell inside the container:

```sh
./cli-duoglotcompare.sh
```

Then run the following on the container's shell to enter the `py39` conda environment where JavaScripthon is already installed:

```
cd /workspace/data/duoglot/comparisons/try_JavaScripthon/
conda activate py38
```

Then run command `python -m metapensiero.pj -h` to check if JavaScripthon is working:
```
(py38) python -m metapensiero.pj -h
usage: pj [-h] [--disable-es6] [--disable-stage3] [-5] [--transform-runtime] [-o OUTPUT] [-d] [--pdb] [-s STRING] [-e] [--dump-ast] [--inline-map] [--source-name SOURCE_NAME] [file [file ...]]

A Python 3.5+ to ES6 JavaScript compiler
...
```

## Evaluate JavaScripthon on GFG benchmarks

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_gfg.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_javascripthon_original.py trans >eval_javascripthon_original.trans.out.log 2>eval_javascripthon_original.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_javascripthon_original.trans.out.log | grep TRANSTIME > eval_javascripthon_original.trans.time.log
  cat eval_javascripthon_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness (59 `cannot-translate` errors expected before testing)
  ```sh
  python3 eval_javascripthon_original.py fill
  python3 eval_javascripthon_original.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_javascripthon_original.py stat showerr > ./eval_javascripthon_original.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./standalone
  chmod 777 ./eval*.log
  ```

### **Where to get results?**

- Where to get correct rate and list of failed benchmarks?  
  Open `eval_javascripthon_original.stat.log` and scroll to the bottom. You should be able to see this (The number might have minor differences due to different versions of python or node installed):
  ```log
  ...
  SHOWERR: GFG_TRIANGULAR_NUMBERS_1.py
  SHOWERR: GFG_UGLY_NUMBERS.py
  SHOWERR: GFG_UNIQUE_CELLS_BINARY_MATRIX.py
  SHOWERR: GFG_WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS.py
  SHOWERR: GFG_WRITE_AN_EFFICIENT_METHOD_TO_CHECK_IF_A_NUMBER_IS_MULTIPLE_OF_3.py
  SHOWERR: GFG_WRITE_ONE_LINE_C_FUNCTION_TO_FIND_WHETHER_A_NO_IS_POWER_OF_TWO.py
  Write file: ./eval_javascripthon_solved_set.json
  ratio: 0.42550143266475643  skipcount: 0  executor_err_count: 1  test_err_count: 401
  ```
  - `ratio` is the correct rate. `0.4255` means 42.55% of the translation pass the tests.
  - Lines start with `SHOWERR` are the failed benchmarks. 

- Where to get timing?  
  Open `eval_javascripthon_original.trans.time.log`. The timing of each benchmark is shown at the end of the line:
  ```log
  (GFG_ADD_1_TO_A_GIVEN_NUMBER.py) TRANSTIME:0.2659266544505954
  (GFG_ADD_1_TO_A_GIVEN_NUMBER_1.py) TRANSTIME:0.21650961693376303
  (GFG_ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS.py) TRANSTIME:0.2662813672795892
  (GFG_ALTERNATIVE_SORTING.py) TRANSTIME:0.2160875564441085
  (GFG_ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS.py) TRANSTIME:0.26679854467511177
  ...
  ```
  To get the average timing, please run the second command in the step 2 above.

- Where to check intermediate logs and results for debugging?
  - translator's `stdout`: `eval_javascripthon_original.trans.out.log`
  - translator's `stderr`: `eval_javascripthon_original.trans.err.log`
  - Python code to be translated: `./standalone/pygold/GFG*.py`
  - Translated JavaScript (raw): `./standalone/pygold/GFG*.js`
  - Translated JavaScript wrapped for testing: `./standalone/combined/GFG*.js`
  - Test output of translated JavaScript: `./standalone/output/GFG*.js.err` and `./standalone/output/GFG*.js.out`


## Evaluate JavaScripthon on Case Study 1 - LeetCode

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_leetcode.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_javascripthon_main.py trans >eval_javascripthon_main.trans.out.log 2>eval_javascripthon_main.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_javascripthon_main.trans.out.log | grep TRANSTIME > eval_javascripthon_main.trans.time.log
  cat eval_javascripthon_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness (492 `cannot-translate` error expected  before testing)
  ```sh
  python3 eval_javascripthon_main.py fill
  python3 eval_javascripthon_main.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_javascripthon_main.py showerr stat > ./eval_javascripthon_main.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./staleetcode/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_javascripthon_original.*.log`, looking at `eval_javascripthon_main.*.log` to see the results for `LeetCode`. 
- **Note that the following correct rate `0.0` it is expected** due to JavaScripthon not capable of handling newer Python language features such as type annotations:
  ```
  ratio: 0.0  skipcount: 0  executor_err_count: 0  test_err_count: 1067
  ```
- Instead of looking into the folder `standalone` for detailed output, looking into the `staleetcode` folder.

## Evaluate JavaScripthon on Case Study 2 - CtCI

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_ctci.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_javascripthon_ctci.py trans >eval_javascripthon_ctci.trans.out.log 2>eval_javascripthon_ctci.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_javascripthon_ctci.trans.out.log | grep TRANSTIME > eval_javascripthon_ctci.trans.time.log
  cat eval_javascripthon_ctci.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following 2 commands to wrap the translation with tests and test the translation for checking correctness (18 `cannot translate` error expected)
  ```sh
  python3 eval_javascripthon_ctci.py fill
  python3 eval_javascripthon_ctci.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_javascripthon_ctci.py showerr stat > ./eval_javascripthon_ctci.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./stactci/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_javascripthon_original.*.log`, looking at `eval_javascripthon_ctci.*.log` to see the results for `LeetCode`. The correct rate should be 8%:
  ```
  ratio: 0.08  skipcount: 0  executor_err_count: 0  test_err_count: 23
  ``` 
- Instead of looking into the folder `standalone` for detailed output, looking into the `stactci` folder.

