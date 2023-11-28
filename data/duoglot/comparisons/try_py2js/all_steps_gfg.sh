# --- step 0 ---
cd /workspace/data/duoglot/comparisons/try_py2js/
# conda activate py27
python2 /root/py2js/pyjs.py -h

# --- step 1 ---
python3 eval_py2js_original.py trans >eval_py2js_original.trans.out.log 2>eval_py2js_original.trans.err.log

# --- step 2 ---
cat eval_py2js_original.trans.out.log | grep TRANSTIME > eval_py2js_original.trans.time.log
cat eval_py2js_original.trans.time.log | awk '{print $2}' | awk -F: '{sum+=$2} END {print sum/NR}'

# --- step 3 ---
python3 eval_py2js_original.py fill
python3 eval_py2js_original.py run

# --- step 4 ---
python3 eval_py2js_original.py stat showerr > ./eval_py2js_original.stat.log

# --- step 5 ---
chmod 777 -R ./standalone
chmod 777 ./eval*.log
