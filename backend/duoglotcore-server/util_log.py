import os
import json

LOGDIR = "./logs"

def _get_log_filename(filename):
  return os.path.join(LOGDIR, filename)

class SetEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, set):
      return str(obj)
    return json.JSONEncoder.default(self, obj)

def log_json(key, jobj):
  fname = _get_log_filename(key + ".json")
  # print(f"# Logging JSON to {fname} (NOTICE: Not for accurate serializing)...")
  with open(fname, 'w') as f:
    json.dump(jobj, f, cls=SetEncoder, indent=1)
