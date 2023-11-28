# Evaluating Codex

## Entering the evaluation environment for Codex 

First run the following command inside the folder `<RepoRoot>/docker/thirdparty/` to start `duoglotcompare` container and obtain a bash shell inside the container:

```sh
./cli-duoglotcompare.sh
```

Then run the following on the container's shell to enter the `base` conda environment where `openai` (the python package for accessing Codex) is already installed:

```
cd /workspace/data/duoglot/comparisons/try_codex/
conda activate base
```

Then run command `pip list | grep openai` to check if `openai` is there:
```
openai    0.25.0
```


## Set OpenAI API Token

Codex is a large language model provided by [OpenAI](https://openai.com/api/). To be able to query the API, you need to be able to access to model id `code-davinci-001`/`code-davinci-002`. 

**NOTICE: The experiments in the paper was based on `code-davinci-001`, but at the time of releasing this artifact, `code-davinci-002` is also available. If you are have free beta access to `code-davinci-002`, you can use `code-davinci-002` and it performs better than `code-davinci-001`.**

To set the API token, please do the following steps:  

1. Get the token from OpenAI. Login to OpenAI -> `Personal` (Right-top-corner) -> `View API Keys` -> `Create new secret key` and copy the key.

2. Create a file beside `eval_codex*.py` (inside `try_codex` folder) named `drvtry`. The content of the file is the key inside double quote:
    ```json
    "sk-9vFW......dRO"
    ```

3. Run `test_codex.py`. Following output indicates that `Codex` can be normally accessed.
    ```
    ----- SUCCESSFUL -----

    function f_gold (mat, r, c) {
      var result = 0;
      for (var i = 0; i < r; i++) {
        var j = 0;
        ...
    ```

    If it is not working, modify line 48 of `test_codex.py` to use `code-davinci-002`. If `code-davinci-002` is working then you can do experiments based on `code-davinci-002`.

4. (Optional) Check your maximum tokens-per-query allowed.  
    Modify line 50 of `test_codex.py`. Change it to some large number such as `5432`. if you get the following:  
    
    ```
    openai.error.RateLimitError: Rate limit reached for default-codex in organization org-XXXXX on tokens per min. Limit: 40000.000000 / min. Current: 54320.000000 / min. .....
    ```

    Then it means that you can query at most 4000 tokens per query. If your limit is less than 4000, you might not be able to finish running the experiments. 

    If you try `max_tokens = 4000` and get:
    ```
    openai.error.InvalidRequestError: This model's maximum context length is 4097 tokens, however you requested 4162 tokens (162 in your prompt; 4000 for the completion).
    ```

    Then it means that the model you are using `codex-davinci-001` can only handle up to 4097 tokens (prompt length + completion `max_tokens`). It is normal and the evaluation script will handle this error and retry with reduced `max_tokens`.

## Evaluate Codex on GFG benchmarks

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_gfg.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to create configuration folder and the prompts for Codex to complete
  ```sh
  export CODEX_CONFIG_NAME=temp0-prompt1-model001
  # export CODEX_CONFIG_NAME=temp0-prompt1-model002
  python3 eval_codex_original.py $CODEX_CONFIG_NAME gold
  ```

- **Step 2**: Run the following to call Codex to get translations (This operation might take several hours)

  ```sh
  expect /usr/bin/unbuffer python3 eval_codex_original.py $CODEX_CONFIG_NAME trans >>eval_codex_original.trans.$CODEX_CONFIG_NAME.log
  ```

- **Step 3**: Run the following to collect timing
  ```sh
  cat eval_codex_original.trans.$CODEX_CONFIG_NAME.log | grep TRANSTIME > eval_codex_original.trans.$CODEX_CONFIG_NAME.time.log
  cat eval_codex_original.trans.$CODEX_CONFIG_NAME.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 4**: Run the following 2 commands to extract the translation and cleanup the translation. It is normal to have dozens of `not_finished_or_unexpected` shown in the end of the log.
  ```sh
  python3 eval_codex_original.py $CODEX_CONFIG_NAME extract
  python3 eval_codex_original.py $CODEX_CONFIG_NAME transclean
  ```

  For example, the end of the log below shows that there are 47 unexpected or incomplete translations:
  ```sh
  ...
  Write file: standalone-codex-temp0-prompt1-model001/./trans/GFG_ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION.clean.js
  Write file: standalone-codex-temp0-prompt1-model001/./trans/GFG_ZECKENDORFS_THEOREM_NON_NEIGHBOURING_FIBONACCI_REPRESENTATION.clean.fix.js
  not_exist_count: 0  not_finished_or_unexpected_count: 47
  ```

- **Step 5**: Run the following command to redo translation of `not_finished_or_unexpected` cases with maximum token length:

  ```sh
  expect /usr/bin/unbuffer python3 eval_codex_original.py $CODEX_CONFIG_NAME trans_maximum >>eval_codex_original.trans_maximum.$CODEX_CONFIG_NAME.log
  ```

- **Step 6**: Run the following commands again to extract and cleanup translations

  ```sh
  python3 eval_codex_original.py $CODEX_CONFIG_NAME extract
  python3 eval_codex_original.py $CODEX_CONFIG_NAME transclean
  ```

- **Step 7**: Run the following to wrap translations with tests and run all tests to check for correctness
  ```sh
  python3 eval_codex_original.py $CODEX_CONFIG_NAME fill
  python3 eval_codex_original.py $CODEX_CONFIG_NAME run
  ```

- **Step 8**: Run the following to collect errors
  ```sh
  python3 eval_codex_original.py $CODEX_CONFIG_NAME stat > eval_codex_original.trans.$CODEX_CONFIG_NAME.stat.log
  ```

  If you are using `code-davinci-001`, you should be able to get correct rate 75%:
  ```
  Write file: ./eval_codex_solved_set.clean.js.json
  ratio: 0.3132183908045977  skipcount: 0  norun_count: 3  executor_err_count: 0  pass_count: 218  test_err_count: 478
  Write file: ./eval_codex_solved_set.clean.fix.js.json
  ratio: 0.7456896551724138  skipcount: 0  norun_count: 3  executor_err_count: 0  pass_count: 519  test_err_count: 177
  ```


- **Step 9**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./standalone-*
  chmod 777 ./eval*.log
  ```


## Evaluate Codex on Case Study 1 - LeetCode

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_leetcode.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results.

- **Step 1**: Run the following to create configuration folder and the prompts for Codex to complete 
  ```sh
  export CODEX_CONFIG_NAME=temp0-prompt1-model001
  # export CODEX_CONFIG_NAME=temp0-prompt1-model001
  python3 eval_codex_main.py $CODEX_CONFIG_NAME gold
  ```

- **Step 2**: Run the following to call Codex to get translations (This operation might take several hours)  
  ```sh
  expect /usr/bin/unbuffer python3 eval_codex_main.py $CODEX_CONFIG_NAME trans >>eval_codex_main.trans.$CODEX_CONFIG_NAME.log
  ```

- **Step 3**: Run the following to collect timing
  ```sh
  cat eval_codex_main.trans.$CODEX_CONFIG_NAME.log | grep TRANSTIME > eval_codex_main.trans.$CODEX_CONFIG_NAME.time.log
  cat eval_codex_main.trans.$CODEX_CONFIG_NAME.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 4**: Run the following 2 commands to extract the translation and cleanup the translation. It is normal to have dozens of `not_finished_or_unexpected` shown in the end of the log.
  ```sh
  python3 eval_codex_main.py $CODEX_CONFIG_NAME extract
  python3 eval_codex_main.py $CODEX_CONFIG_NAME transclean
  ```

  For example, the end of the log shows that 62 of the translation might not be complete:
  ```log
  ...
  Write file: staleetcode-codex-temp0-prompt1-model001/./trans/L2321_MaximumScoreOfSplicedArray.clean.fix.js
  FAILED TO CLEAN: staleetcode-codex-temp0-prompt1-model001/./trans/L2322_MinimumScoreAfterRemovalsonaTree.txt
  Write file: staleetcode-codex-temp0-prompt1-model001/./trans/L2323_FindMinimumTimetoFinishAllJobsII.clean.js
  Write file: staleetcode-codex-temp0-prompt1-model001/./trans/L2323_FindMinimumTimetoFinishAllJobsII.clean.fix.js
  not_exist_count: 0  not_finished_or_unexpected_count: 62
  ```

- **Step 5**: Run the following command to redo translation of `not_finished_or_unexpected` cases with maximum token length:  
  ```sh
  expect /usr/bin/unbuffer python3 eval_codex_main.py $CODEX_CONFIG_NAME trans_maximum >>eval_codex_main.trans_maximum.$CODEX_CONFIG_NAME.log
  ```

- **Step 6**: Run the following commands again to extract and cleanup translations  
  ```sh
  python3 eval_codex_main.py $CODEX_CONFIG_NAME extract
  python3 eval_codex_main.py $CODEX_CONFIG_NAME transclean
  ```

- **Step 7**: Run the following to wrap translations with tests and run all tests to check for correctness  
  ```sh
  python3 eval_codex_main.py $CODEX_CONFIG_NAME fill
  python3 eval_codex_main.py $CODEX_CONFIG_NAME run
  ```

- **Step 8**: Run the following to collect errors
  ```sh
  python3 eval_codex_main.py $CODEX_CONFIG_NAME stat > eval_codex_main.trans.$CODEX_CONFIG_NAME.stat.log
  ```

  For example, you might see numbers similar to the following at the end of log. It means that after cleaning up and fixing function names, the correct rate is `49.5%` if you are using `code-davinci-001`.

  Using `code-davinci-001`:  
  ```log
  Write file: ./eval_codex_solved_set.clean.js.json
  ratio: 0.0647279549718574  skipcount: 0  norun_count: 1  executor_err_count: 0  pass_count: 69  test_err_count: 997
  Write file: ./eval_codex_solved_set.clean.fix.js.json
  ratio: 0.49530956848030017  skipcount: 0  norun_count: 1  executor_err_count: 0  pass_count: 528  test_err_count: 538
  ```


- **Step 9**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./standalone-*
  chmod 777 ./eval*.log
  ```


## Evaluate Codex on Case Study 2 - CtCI

All the steps below are performed inside the `duoglotcompare` container.

All the following steps are concatenated in `all_steps_ctci.sh`. You can run the script to reproduce the results. Alternatively, you can follow the steps below to check intermediate results. However, one of the steps (Step 4) cannot be automated so far. The translation result is noisy and needs manual inspection and manual cleanup.

- **Step 1**: Run the following to create configuration folder and the prompts for Codex to complete

  ```sh
  export CODEX_CONFIG_NAME=temp0-prompt1-model001
  # export CODEX_CONFIG_NAME=temp0-prompt1-model002
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME gold
  ```

- **Step 2**: Run the following to call Codex to get translations (This operation might take an hour)
  ```sh
  expect /usr/bin/unbuffer python3 eval_codex_ctci.py $CODEX_CONFIG_NAME trans >>eval_codex_ctci.trans.$CODEX_CONFIG_NAME.log
  ```

- **Step 3**: Run the following to collect timing  
  ```sh
  cat eval_codex_ctci.trans.$CODEX_CONFIG_NAME.log | grep TRANSTIME > eval_codex_ctci.trans.$CODEX_CONFIG_NAME.time.log
  cat eval_codex_ctci.trans.$CODEX_CONFIG_NAME.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'
  ```

- **Step 4**: Run the following 2 commands to extract the translation and cleanup the translation. **NOTE: For CtCI, the first pass of translation is already setting max_tokens to maximum. Thus, there's no second pass of translation for non-complete translation.**

  ```sh
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME extract
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME transcleanman
  ```

- **Step 5**: Run the following to wrap translations with tests and run all tests to check for correctness
  ```sh
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME fill
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME run
  ```

- **Step 6**: Run the following to collect errors
  ```sh
  python3 eval_codex_ctci.py $CODEX_CONFIG_NAME showerr stat > eval_codex_ctci.trans.$CODEX_CONFIG_NAME.stat.log
  ```
  You might see this at the end of the `stat.log`. However, the actual correct rate is not 41.6% due to wrongly translated test code. The details of manual validation is shown at the end of this document.
  ```
  ratio: 0.4166666666666667  skipcount: 0  norun_count: 1  executor_err_count: 0  pass_count: 10  test_err_count: 14
  ```
  

- **Step 7**: Run the following to change file permissions
  ```sh
  chmod 777 -R ./stactci-*
  chmod 777 ./eval*.log
  ```



### CtCI Manual Result Validation Results

Only 3 translations are correct:
- AL066
- AL071
- AL081_p01_route 


Others are wrong. 
```
SHOWERR: AL054_p02_robot_grid.py
MANUAL VALIDATION ERROR: AL064
SHOWERR: AL067_p03_delete_middle_node.py
MANUAL VALIDATION ERROR: AL070 inf loop
SHOWERR: AL072_p06_animal_shelter.py
SHOWERR: AL074_p04_palindrome_permutation.py
SHOWERR: AL080_p03_search_in_rotated_array.py
MANUAL VALIDATION ERROR: AL081_p05_recursive
SHOWERR: AL082_p07_intersection.py
MANUAL VALIDATION ERROR: AL083_p08_loop_detection
SHOWERR: AL083_p01_is_unique
SHOWERR: AL086_p06_successor.py
MANUAL VALIDATION ERROR: AL089 mismatch
SHOWERR: AL090_p08_english_int.py
SHOWERR: AL092_p02_return_kth_to_last.py
SHOWERR: AL103_p03_stack_of_plates.py
SHOWERR: AL113_p05_validate_bst.py
SHOWERR: AL122_p04_check_balanced.py
MANUAL VALIDATION ERROR: AL123 result mismatch
SHOWERR: AL125_p03_list_of_depths.py
SHOWERR: AL160_p06_palindrome.py
MANUAL VALIDATION ERROR: AL1001
```


AL089 get:
```
[ '(())', '()()' ]
[ '((()))' ]
[ '((()))', '(()())', '(())()', '()(())', '()()()' ]
```

AL089 expected:
```
[ '(())', '()()' ]
[ '((()))', '(()())', '(())()', '()(())', '()()()' ]
[ '((()))', '(()())', '(())()', '()(())', '()()()' ]
```

AL123 mismatch output:
```
[
  [ 20, 9, 25, 5, 12 ],
  [ 20, 9, 25, 12, 5 ],
  [ 20, 9, 5, 25, 12 ],
  [ 20, 9, 5, 12, 25 ],
  [ 20, 9, 12, 25, 5 ],
  [ 20, 9, 12, 5, 25 ],
  [ 20, 25, 9, 5, 12 ],
  [ 20, 25, 9, 12, 5 ]
]
[
  [ 20, 9, 25, 5, 12 ],
  [ 20, 9, 25, 12, 5 ],
  [ 20, 9, 5, 25, 12 ],
  [ 20, 9, 5, 12, 25 ],
  [ 20, 9, 12, 25, 5 ],
  [ 20, 9, 12, 5, 25 ],
  [ 20, 25, 9, 5, 12 ],
  [ 20, 25, 9, 12, 5 ]
]
```

Corresponding python:
```
[
  [20, 9, 5, 12, 25], 
  [20, 9, 5, 25, 12], 
  [20, 9, 25, 5, 12], 
  [20, 25, 9, 5, 12], 
  [20, 9, 12, 5, 25], 
  [20, 9, 12, 25, 5], 
  [20, 9, 25, 12, 5], 
  [20, 25, 9, 12, 5]
]
[
  [20, 9, 25, 5, 12], 
  [20, 9, 25, 12, 5], 
  [20, 9, 5, 25, 12], 
  [20, 9, 5, 12, 25], 
  [20, 9, 12, 25, 5], 
  [20, 9, 12, 5, 25], 
  [20, 25, 9, 5, 12], 
  [20, 25, 9, 12, 5]
]
```
