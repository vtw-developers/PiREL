# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_JavaScripthon/
# conda activate py38
python -m metapensiero.pj -h

# --- step 1 ---
python3 eval_javascripthon_main.py trans >eval_javascripthon_main.trans.out.log 2>eval_javascripthon_main.trans.err.log

# --- step 2 ---
cat eval_javascripthon_main.trans.out.log | grep TRANSTIME > eval_javascripthon_main.trans.time.log
cat eval_javascripthon_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_javascripthon_main.py fill
python3 eval_javascripthon_main.py run

# --- step 4 ---
python3 eval_javascripthon_main.py showerr stat > ./eval_javascripthon_main.stat.log

# --- step 5 ---
chmod -R 777 ./staleetcode/
chmod 777 ./eval*.log
