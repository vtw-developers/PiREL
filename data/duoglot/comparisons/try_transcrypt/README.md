# Evaluating Transcrypt

## Entering the evaluation environment for Transcrypt 

First run the following command inside the folder `<RepoRoot>/docker/thirdparty/` to start `duoglotcompare` container and obtain a bash shell inside the container:

```sh
./cli-duoglotcompare.sh
```

Then run the following on the container's shell to enter the `py39` conda environment where Transcrypt is already installed:

```
cd /workspace/data/duoglot/comparisons/try_transcrypt/
conda activate py39
```

Then run command `transcrypt -h` to check if Transcrypt is working:
```
Transcrypt (TM) Python to JavaScript Small Sane Subset Transpiler Version 3.9.0
Copyright (C) Geatec Engineering. License: Apache 2.0


usage: transcrypt ...
```

## Evaluate Transcrypt on GFG benchmarks

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_gfg.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_transcrypt_original.py trans >eval_transcrypt_original.trans.out.log 2>eval_transcrypt_original.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_transcrypt_original.trans.out.log | grep TRANSTIME > eval_transcrypt_original.trans.time.log
  cat eval_transcrypt_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following to test the translation for checking correctness
  ```sh
  python3 eval_transcrypt_original.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_transcrypt_original.py stat showerr > ./eval_transcrypt_original.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./standalone
  chmod 777 ./eval*.log
  ```

### **Where to get results?**

- Where to get correct rate and list of failed benchmarks?  
  Open `eval_transcrypt_original.stat.log` and scroll to the bottom. You should be able to see this (The number might have minor differences due to different versions of python or node installed):
  ```log
  ...
  SHOWERR: GFG_UGLY_NUMBERS.py
  SHOWERR: GFG_UNIQUE_CELLS_BINARY_MATRIX.py
  SHOWERR: GFG_WAYS_TRANSFORMING_ONE_STRING_REMOVING_0_CHARACTERS.py
  Write file: ./eval_transcrypt_solved_set.json
  ratio: 0.759018759018759  skipcount: 0  executor_err_count: 6  test_err_count: 167
  ```
  - `ratio` is the correct rate. `0.759` means 75.9% of the translation pass the tests.
  - Lines start with `SHOWERR` are the failed benchmarks. 

- Where to get timing?  
  Open `eval_transcrypt_original.trans.time.log`. The timing of each benchmark is shown at the end of the line:
  ```log
  (GFG_ADD_1_TO_A_GIVEN_NUMBER.py) TRANSTIME:0.2663212325423956
  (GFG_ADD_1_TO_A_GIVEN_NUMBER_1.py) TRANSTIME:0.2164915632456541
  (GFG_ADD_TWO_NUMBERS_WITHOUT_USING_ARITHMETIC_OPERATORS.py) TRANSTIME:0.2661356804892421
  (GFG_ALTERNATIVE_SORTING.py) TRANSTIME:0.26634142734110355
  (GFG_ANALYSIS_OF_ALGORITHMS_SET_2_ASYMPTOTIC_ANALYSIS.py) TRANSTIME:0.21615517511963844
  ...
  ```
  The average timing can be obtained by running the second command in the step 2 above.

- Where to check intermediate logs and results for debugging?
  - translator's `stdout`: `eval_transcrypt_original.trans.out.log`
  - translator's `stderr`: `eval_transcrypt_original.trans.err.log`
  - Python code to be translated: `./standalone/pygold/GFG*.py`
  - Translated JavaScript (raw): `./standalone/combined/GFG*/GFG*.js.backup`
  - Translated JavaScript wrapped for testing: `./standalone/combined/GFG*/GFG*.js`
  - Test output of translated JavaScript: `./standalone/output/GFG*.js.err` and `./standalone/output/GFG*.js.out`


## Evaluate Transcrypt on Case Study 1 - LeetCode

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_leetcode.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_transcrypt_main.py trans >eval_transcrypt_main.trans.out.log 2>eval_transcrypt_main.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_transcrypt_main.trans.out.log | grep TRANSTIME > eval_transcrypt_main.trans.time.log
  cat eval_transcrypt_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following to test the translation for checking correctness
  ```sh
  python3 eval_transcrypt_main.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_transcrypt_main.py showerr stat > ./eval_transcrypt_main.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./staleetcode/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_transcrypt_original.*.log`, looking at `eval_transcrypt_main.*.log` to see the results for `LeetCode`. 
- Instead of looking into the folder `standalone` for detailed output, looking into the `staleetcode` folder.

## Evaluate Transcrypt on Case Study 2 - CtCI

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_ctci.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to translate python files
  ```sh
  python3 eval_transcrypt_ctci.py trans >eval_transcrypt_ctci.trans.out.log 2>eval_transcrypt_ctci.trans.err.log
  ```

- **Step 2**: Run the following to collect timing
  ```sh
  cat eval_transcrypt_ctci.trans.out.log | grep TRANSTIME > eval_transcrypt_ctci.trans.time.log
  cat eval_transcrypt_ctci.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 3**: Run the following to test the translation for checking correctness
  ```sh
  python3 eval_transcrypt_ctci.py run
  ```

- **Step 4**: Run the following to collect errors
  ```sh
  python3 eval_transcrypt_ctci.py showerr stat > ./eval_transcrypt_ctci.stat.log
  ```

- **Step 5**: Run the following to change file permissions
  ```sh
  chmod -R 777 ./stactci/
  chmod 777 ./eval*.log
  ```

### Where to get results?

Similar to the `GFG Benchmarks` in the previous section. Differences:
- Instead of looking at `eval_transcrypt_original.*.log`, looking at `eval_transcrypt_ctci.*.log` to see the results for `LeetCode`. 
- Instead of looking into the folder `standalone` for detailed output, looking into the `stactci` folder.
- **The automatically computed correct rate is not accurate**, because `CtCI` programs' tests are mixed with the code being tested, and some tests can be wrongly translated. Thus, we provide the result of our manual validation of passed CtCI benchmarks:  
  - "AL054_p02_robot_grid"  OK.
  - "AL067_p03_delete_middle_node"  OK.
  - "AL072_p06_animal_shelter"  OK.
  - "AL081_p07_intersection"  OK.
  - "AL083_p08_loop_detection"  OK.
  - "AL086_p06_successor"  OK.
  - ~~"AL090_p08_english_int"~~ NOT CORRECT.
  - "AL092_p02_return_kth_to_last"  OK.
  - "AL113_p05_validate_bst"  OK.
  - "AL122_p04_check_balanced"  OK.
  - "AL160_p06_palindrome"  OK.


