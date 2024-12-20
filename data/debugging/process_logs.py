"""
REQUIRED DIRECTORY STRUCTURE FOR THE LOGS GENERATED BY PIREL-LEARN-RULES MODE:
- backend/
  - file artifacts generated in backend/duoglotcore-server/pirel-logs (format before moving)
- frontend/
  - directories copied from data/logs-learn-rules (L*) (format before moving)
  - *.json files (format before moving)
- rules/
  - all learned rules per subject copied from data/duoglot/tests/trans_programs/py_js
- this script
- pirel.log from backend/duoglotcore-server/pirel-logs

USAGE:
1. copy this script into logs directory
2. run

NOTES:
1. refer to learnRules_ns.runSingleProgram() for more details on `programTranslationState`

REQUIREMENTS:
pip install levenshtein
pip install scikit-learn
pip install numpy
"""

import json
import os
import re
import shutil
from pathlib import Path
from typing import List, Dict, Tuple

import numpy as np
from sklearn.cluster import dbscan
from Levenshtein import distance


CWD = Path(__file__).parent
EPS = 1e-3
EPS = 40


def read_json(fpath):
  with open(fpath) as fin:
    json_obj = json.loads(fin.read())
    return json_obj


def pirel_error_to_str(error: dict) -> str:
  '''POST: return value can be rendered as bash markdown code block'''
  result = ''
  for k, v in error.items():
    result += f'# {str(k)}:\n{str(v)}\n'
  return result.strip()


def cluster_str_sequence(seq: List[str], eps=1e-1) -> Dict[int, List[str]]:
  '''
  PRE: len(seq) >= 2
  '''
  def _lev_metric(x, y):
    i, j = int(x[0]), int(y[0])     # extract indices
    return distance(seq[i], seq[j])
  # actual clustering algorithm
  X = np.arange(len(seq)).reshape(-1, 1)
  idxs, clusters = dbscan(X, metric=_lev_metric, eps=eps, min_samples=2)
  # preparing data to return
  return_dict = {}
  for str_elem, cluster in zip(seq, clusters):
    return_dict.setdefault(cluster, []).append(str_elem)
  return return_dict


def program_translation_state_to_md(log_fpath: Path) -> Tuple[str, str]:
  '''return str(translation_state), error (for clustering), trans_is_successful'''
  subject_id = log_fpath.parent.stem
  trans_log = read_json(log_fpath)
  trans_is_successful = trans_log['success']
  if trans_is_successful:
    error = ''
  else:
    error = f'# SUBJECT: {subject_id}\n' + pirel_error_to_str(json.loads(trans_log['error']))

  result_str = f'## {subject_id} (success = {trans_is_successful})\n'
  if error:
    result_str += f'### Error\n'
    result_str += f'```bash\n{error}\n```\n'
  else:
    result_str += f'### No Error\n'
  result_str += '\n'

  return result_str, error, trans_is_successful


def summarize_learn_rules_results():
  fout = open('summary.md', 'w')
  FRONTEND_DIR = CWD / 'frontend'
  log_fpaths = list(sorted(FRONTEND_DIR.glob('**/*program-translation-state.json')))

  subject_mds = []
  error_msgs = []  # for clustering
  count_successful = 0
  count_all = len(log_fpaths)
  summary_contents = ''

  # section 1 (subjects)
  for log_fpath in log_fpaths:
    subject_md, error, trans_is_successful = program_translation_state_to_md(log_fpath)
    subject_mds.append(subject_md)
    error_msgs.append(error)
    count_successful += int(trans_is_successful)

  summary_contents += f'# Subjects ({count_successful}/{count_all} successful)\n\n'
  summary_contents += ''.join(subject_mds)

  # section 2 (clusters)
  summary_contents += f'# Error Clusters (eps={EPS})\n\n'
  clusters = cluster_str_sequence(error_msgs, eps=EPS)
  for cluster_id, errors in sorted(clusters.items(), key=lambda kvpair: len(kvpair[1]), reverse=True):
    summary_contents += f'## Cluster {cluster_id} ({len(errors)} elements)\n'
    for error in errors:
      summary_contents += f'```bash\n{error}\n```\n\n'

  fout.write(summary_contents)
  fout.close()


def _extract_prefixed_logs(prefix: str, entire_log: str) -> str:

  first_log_line_re = re.compile(r'^\d{2}:\d{2}:\d{2},\d+.+$')  # starts with a timestamp
  entire_log = re.sub(r'\n\n+', ' ', entire_log)  # replace consecutive newline characters with a single space character
  
  def __is_log_line(line: str) -> bool:
    '''check if a line is the first line of a single log message'''
    return re.match(first_log_line_re, line) is not None
  
  def __is_prefixed_with(prefix: str, line: str) -> bool:
    chunks = line.split(' ')
    assert __is_log_line(line)
    assert len(chunks) > 4, line  # first four tokens are timestamp, module, level, prefix
    line_prefix = chunks[3]
    return prefix == line_prefix
  
  log_lines = entire_log.split('\n')
  prefix_lines = []
  is_accepting_lines = False  # is accepting multiple line log message?
  if __is_log_line(log_lines[0]) and __is_prefixed_with(prefix, log_lines[0]):
    is_accepting_lines = True
    prefix_lines.append(log_lines[0])
    prefix_lines = prefix_lines[1:]
  for log_line in log_lines:
    if is_accepting_lines:
      if not __is_log_line(log_line):
        prefix_lines.append(log_line)
        continue
      if __is_prefixed_with(prefix, log_line):
        prefix_lines.append(log_line)
      else:
        is_accepting_lines = False
    else:
      if not __is_log_line(log_line):
        continue
      if __is_prefixed_with(prefix, log_line):
        prefix_lines.append(log_line)
        is_accepting_lines = True
      else:
        continue
  return '\n'.join(prefix_lines)


def main():
  ''''''
  BACKEND_DIR = CWD / 'backend'

  # 1 get prefixes
  backend_prefixes = ['L0001_TwoSum.py', 'L0003_LongestSubstringWithoutRepeatingCharacters.py', 'L0004_MedianofTwoSortedArrays.py']

  # 2 split file artifacts in backend directory
  for backend_prefix in backend_prefixes:
    backend_prefix_dir = BACKEND_DIR / backend_prefix
    os.makedirs(backend_prefix_dir, exist_ok=True)
    for backend_fpath in BACKEND_DIR.iterdir():
      if not backend_fpath.is_file():
        continue
      # NOTE if prefix is not a unique token, then we might have an issue
      if backend_prefix in backend_fpath.stem:
        shutil.copy(backend_fpath, backend_prefix_dir)

  # 3 split pirel.log log file
  os.makedirs('logs', exist_ok=True)
  with open('pirel.log') as fin:
    log_contents = fin.read()
  for backend_prefix in backend_prefixes:
    backend_prefix_fout = open(f'logs/{backend_prefix}.log', 'w')
    prefixed_log = _extract_prefixed_logs(backend_prefix, log_contents)
    backend_prefix_fout.write(prefixed_log)
    backend_prefix_fout.close()

  # 4 prepare summary.md
  summarize_learn_rules_results()


if __name__ == '__main__':
  main()
