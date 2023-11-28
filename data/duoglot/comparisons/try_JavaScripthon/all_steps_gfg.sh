# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_JavaScripthon/
# conda activate py38
python -m metapensiero.pj -h

# --- step 1 ---
python3 eval_javascripthon_original.py trans >eval_javascripthon_original.trans.out.log 2>eval_javascripthon_original.trans.err.log

# --- step 2 ---
cat eval_javascripthon_original.trans.out.log | grep TRANSTIME > eval_javascripthon_original.trans.time.log
cat eval_javascripthon_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_javascripthon_original.py fill
python3 eval_javascripthon_original.py run

# --- step 4 ---
python3 eval_javascripthon_original.py stat showerr > ./eval_javascripthon_original.stat.log

# --- step 5 ---
chmod 777 -R ./standalone
chmod 777 ./eval*.log
