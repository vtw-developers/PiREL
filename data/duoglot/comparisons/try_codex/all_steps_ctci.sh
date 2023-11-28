# --- step 1 ---
export CODEX_CONFIG_NAME=temp0-prompt1-model001
# export CODEX_CONFIG_NAME=temp0-prompt1-model002
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME gold

# --- step 2 ---
expect /usr/bin/unbuffer python3 eval_codex_ctci.py $CODEX_CONFIG_NAME trans >>eval_codex_ctci.trans.$CODEX_CONFIG_NAME.log

# --- step 3 ---
cat eval_codex_ctci.trans.$CODEX_CONFIG_NAME.log | grep TRANSTIME > eval_codex_ctci.trans.$CODEX_CONFIG_NAME.time.log
cat eval_codex_ctci.trans.$CODEX_CONFIG_NAME.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 4 ---
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME extract
# NOTE: The following command requires human intervention to clean the translations.
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME transcleanman

# --- step 5 ---
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME fill
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME run

# --- step 6 ---
python3 eval_codex_ctci.py $CODEX_CONFIG_NAME showerr stat > eval_codex_ctci.trans.$CODEX_CONFIG_NAME.stat.log

# --- step 7 ---
chmod 777 -R ./stactci-*
chmod 777 ./eval*.log
