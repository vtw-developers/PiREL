# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_transcrypt/
conda activate py39
transcrypt -h

# --- step 1 ---
python3 eval_transcrypt_main.py trans >eval_transcrypt_main.trans.out.log 2>eval_transcrypt_main.trans.err.log

# --- step 2 ---
cat eval_transcrypt_main.trans.out.log | grep TRANSTIME > eval_transcrypt_main.trans.time.log
cat eval_transcrypt_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_transcrypt_main.py run

# --- step 4 ---
python3 eval_transcrypt_main.py showerr stat > ./eval_transcrypt_main.stat.log

# --- step 5 ---
chmod -R 777 ./staleetcode/
chmod 777 ./eval*.log
