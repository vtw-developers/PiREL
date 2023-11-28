# --- step 1 ---
export CODEX_CONFIG_NAME=temp0-prompt1-model001
# export CODEX_CONFIG_NAME=temp0-prompt1-model001
python3 eval_codex_main.py $CODEX_CONFIG_NAME gold

# --- step 2 ---
expect /usr/bin/unbuffer python3 eval_codex_main.py $CODEX_CONFIG_NAME trans >>eval_codex_main.trans.$CODEX_CONFIG_NAME.log

# --- step 3 ---
cat eval_codex_main.trans.$CODEX_CONFIG_NAME.log | grep TRANSTIME > eval_codex_main.trans.$CODEX_CONFIG_NAME.time.log
cat eval_codex_main.trans.$CODEX_CONFIG_NAME.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 4 ---
python3 eval_codex_main.py $CODEX_CONFIG_NAME extract
python3 eval_codex_main.py $CODEX_CONFIG_NAME transclean

# --- step 5 ---
expect /usr/bin/unbuffer python3 eval_codex_main.py $CODEX_CONFIG_NAME trans_maximum >>eval_codex_main.trans_maximum.$CODEX_CONFIG_NAME.log

# --- step 6 ---
python3 eval_codex_main.py $CODEX_CONFIG_NAME extract
python3 eval_codex_main.py $CODEX_CONFIG_NAME transclean

# --- step 7 ---
python3 eval_codex_main.py $CODEX_CONFIG_NAME fill
python3 eval_codex_main.py $CODEX_CONFIG_NAME run

# --- step 8 ---
python3 eval_codex_main.py $CODEX_CONFIG_NAME stat > eval_codex_main.trans.$CODEX_CONFIG_NAME.stat.log

# --- step 9 ---
chmod 777 -R ./staleetcode-*
chmod 777 ./eval*.log
