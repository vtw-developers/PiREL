# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_py2js/
# conda activate py27
python2 /root/py2js/pyjs.py -h

# --- step 1 ---
python3 eval_py2js_main.py trans >eval_py2js_main.trans.out.log 2>eval_py2js_main.trans.err.log

# --- step 2 ---
cat eval_py2js_main.trans.out.log | grep TRANSTIME > eval_py2js_main.trans.time.log
cat eval_py2js_main.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_py2js_main.py fill
python3 eval_py2js_main.py run

# --- step 4 ---
python3 eval_py2js_main.py showerr stat > ./eval_py2js_main.stat.log

# --- step 5 ---
chmod -R 777 ./staleetcode/
chmod 777 ./eval*.log
