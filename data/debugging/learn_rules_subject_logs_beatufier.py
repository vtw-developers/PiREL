"""
USAGE:
1. copy and paste this script into logs generated by the frontend
2. run it to generated a summary of learn-rules mode in parent directory

NOTES:
1. refer to learnRules_ns.runSingleProgram() for more details on `programTranslationState`

REQUIREMENTS:
pip install levenshtein
pip install scikit-learn
pip install numpy
"""

import json
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
  fout = open('../summary.md', 'w')
  log_fpaths = list(sorted(CWD.glob('**/*program-translation-state.json')))

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


if __name__ == '__main__':
  summarize_learn_rules_results()
