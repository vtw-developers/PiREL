# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_transcrypt/
conda activate py39
transcrypt -h

# --- step 1 ---
python3 eval_transcrypt_original.py trans >eval_transcrypt_original.trans.out.log 2>eval_transcrypt_original.trans.err.log

# --- step 2 ---
cat eval_transcrypt_original.trans.out.log | grep TRANSTIME > eval_transcrypt_original.trans.time.log
cat eval_transcrypt_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_transcrypt_original.py run

# --- step 4 ---
python3 eval_transcrypt_original.py stat showerr > ./eval_transcrypt_original.stat.log

# --- step 5 ---
chmod 777 -R ./standalone
chmod 777 ./eval*.log
