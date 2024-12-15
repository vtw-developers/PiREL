'''
PiREL utils
'''

import json
import os
import requests
import logging
from typing import Union, Any, Tuple
from pathlib import Path
import time
from datetime import datetime

import p_consts


logger = logging.getLogger(__name__)


# IO
def read_text(fpath: Union[Path, str]) -> str:
  with open(fpath) as fin:
    return fin.read()

def read_json(fpath: Union[Path, str]) -> Any:
  with open(fpath) as fin:
    return json.loads(fin.read())

def write_text(fpath: Union[Path, str], content: str) -> None:
  write_file(fpath, content, include_timestamp=False)

def write_json(fpath: Union[Path, str], obj: Any) -> None:
  write_file(fpath, json.dumps(obj, default=str), include_timestamp=False)

def write_file(fpath: Union[Path, str], contents: str, include_timestamp=False) -> None:
  ''''''
  assert isinstance(fpath, (Path, str))
  if isinstance(fpath, str):
    fpath = Path(fpath)

  if include_timestamp:
    now_dt = datetime.fromtimestamp(time.time())
    now_st = now_dt.strftime('%m-%d-%H-%M-%S.%f')
    # now_st = now_st[:-3]  # millisecond precision is enough
    fpath = fpath.parent / f'{now_st}-{fpath.name}'

  logger.debug(f'Writing a file to "{fpath}"')
  with open(fpath, 'w') as fout:
    fout.write(contents)


# Helper functions to log directly to a log dir
def log_json(fname: str, obj: Any) -> None:
  write_file(p_consts.LOGS_DIR / fname, json.dumps(obj, default=str), include_timestamp=False)

def log_json_time(fname: str, obj: Any) -> None:
  write_file(p_consts.LOGS_DIR / fname, json.dumps(obj, default=str), include_timestamp=True)

def log_file_time(fname: str, contents: str) -> None:
  write_file(p_consts.LOGS_DIR / fname, contents, include_timestamp=True)


# Parsing and AST related
def does_have_parse_error(content: str, lang: str):
  '''
  As name suggests, use a Tree-sitter parser to parse `content`.
  Return True if there are no parse errors, False otherwise.

  PARAMS
  lang - 'py', 'js'
  '''

  parser = p_consts.PARSER_DICT[lang]
  tree = parser.parse(bytes(content, 'utf8'))
  root_node = tree.root_node
  return root_node.has_error


# Send email notifications
def _get_mailgun_credentials() -> Tuple[str, str]:
  env_fname = '.env.json'
  assert os.path.exists(env_fname), f'Create a "{env_fname}" file with necessary environment variables'
  env_dict = read_json(env_fname)
  try:
    mailgun_api_key = env_dict['MAILGUN_API_KEY']
    mailgun_domain = env_dict['MAILGUN_DOMAIN']
    return mailgun_api_key, mailgun_domain
  except KeyError as err:
    msg = f'An environment variable "{err}" must be set.'
    logger.warning(msg)
    raise err

def send_text_email(subject: str, message: str) -> bool:
  '''Return True if successfully sent, otherwise return False'''
  try:
    mailgun_api_key, mailgun_domain = _get_mailgun_credentials()
  except KeyError:
    logger.warning(f'Not sending an email. Unable to obtain Mailgun credentials.')
    return False

  url = f"https://api.mailgun.net/v3/{mailgun_domain}/messages"
  data = {
    "from": f"Mailgun Sandbox <postmaster@{mailgun_domain}>",
    "to": "Satbek Abdyldayev <satbek@unist.ac.kr>",
    "subject": subject,
    "text": message
  }
  request_obj = requests.post(url, auth=("api", mailgun_api_key), data=data)
  return request_obj.status_code == 200

def email_safely(subject: str, message:str='intentionally left empty') -> bool:
  try:
    result = send_text_email(f'PiREL: {subject}', message)
    if result:
      logger.info('Email notification was sent successfully')
    else:
      logger.warning('Email notification was not sent')
    return result
  except Exception as exc:
    logger.warning(f'Some exception "{exc}" occured in send_text_email()')
    return False
