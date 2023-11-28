# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_JavaScripthon/
# conda activate py38
python -m metapensiero.pj -h

# --- step 1 ---
python3 eval_javascripthon_ctci.py trans >eval_javascripthon_ctci.trans.out.log 2>eval_javascripthon_ctci.trans.err.log

# --- step 2 ---
cat eval_javascripthon_ctci.trans.out.log | grep TRANSTIME > eval_javascripthon_ctci.trans.time.log
cat eval_javascripthon_ctci.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_javascripthon_ctci.py fill
python3 eval_javascripthon_ctci.py run

# --- step 4 ---
python3 eval_javascripthon_ctci.py showerr stat > ./eval_javascripthon_ctci.stat.log

# --- step 5 ---
chmod -R 777 ./stactci/
chmod 777 ./eval*.log
