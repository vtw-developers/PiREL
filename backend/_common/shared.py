import flask
import os

def read_text(fname):
  with open(fname, 'r') as f:
    return f.read()

def gettmpfile_gen(TMPFILE_BASEDIR, app):
  def gettmpfile(filename):
    if filename == "list":
      runner_files = list(os.listdir(TMPFILE_BASEDIR)) if os.path.exists(TMPFILE_BASEDIR) else []
      urls = [(x, os.path.join(TMPFILE_BASEDIR, x)) for x in runner_files]
      links = [f"<a href='./{x[0]}'>{x[0]}</a><br>" for x in urls]
      all_link_str = '\n'.join(links)
      content = f"<html><body><h1>List of files under {TMPFILE_BASEDIR}</h1>{all_link_str}</body></html>"
      response = app.response_class(response=content, status=200, mimetype='text/html')
      return response
    
    fullpath = os.path.join(TMPFILE_BASEDIR, filename)
    try:
      content = read_text(fullpath)
      response = app.response_class(response=content, status=200, mimetype='text/plain')
      return response
    except:
      flask.abort(404)
  return gettmpfile

import traceback
def exception_to_string(excp):
   stack = traceback.extract_tb(excp.__traceback__)  # add limit=??  traceback.extract_stack()[:-3] +
   pretty = traceback.format_list(stack)
   return ''.join(pretty) + '\n  {} {}'.format(excp.__class__,excp)
