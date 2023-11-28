import json
import s_templatizer
from typing import List, Tuple, Union, Dict
from s_data_structures import *
import s_parse_utils
import s_grammar
import sys
import ast_parse


# ~~~ for debugging, can be removed later
import debugpy
def _breakpoint():
  debugpy.listen(('0.0.0.0', 4444))
  debugpy.wait_for_client()
  debugpy.breakpoint()


def read_json(fpath: str) -> dict:
  with open(fpath) as fin:
    return json.loads(fin.read())
def read_file(fpath: str) -> str:
  with open(fpath) as fin:
    return fin.read()
def write_json(fpath: str, json_data: str) -> None:
  with open(fpath, 'w') as fout:
    fout.write(json.dumps(json_data))
def write_file(fpath: str, contents: str) -> None:
  with open(fpath, 'w') as fout:
    fout.write(contents)


# second version of extract_templates
# which allows to generate templates in such a way
# which helps us learn base rules for translation in language-agnostic manner
def extract_templates(
  problematic_ast: list,
  full_ast: list,
  full_ast_text: list,
  ast_annotation: dict,
  lang: str,
  contexts: list
):
  '''
  IDEAS
  - Grow the context starting from the problematic node up until the root node
  - Generate 'shallow' templates

  INTERNAL


  RETURN
  return_data = {
    problematic_node_type: str,
    problematic_node_id: int,
    template_id: {
      template_id: int,
      template_origin: str,
      templatized_node_ids: dict,
      py_block_replaced: bool,
      context_node_type: str,
      template_origin_node_type: str,
      is_valid_template: bool,
      [error: str],
      sub_templates: dict,
      contexts: dict
    },
    num_templates: int
  }

  templatized_node_ids = {
    node_id: path_to_node,
    ...
  }

  sub_templates = {

  }

  contexts = {

  }
  '''

  # this is a temporary block of code
  with open('temporary_problematic_ast.json', 'w') as fout:
    fout.write(json.dumps(problematic_ast))
  with open('temporary_full_ast_text.json', 'w') as fout:
    fout.write(json.dumps(full_ast_text))
  with open('temporary_full_ast.json', 'w') as fout:
    fout.write(json.dumps(full_ast))

  # 1 instantiate a `TemplateTree` - data structure for creating templates
  problematic_node_id = problematic_ast[1]
  template_tree = s_templatizer.TemplateTree(full_ast_text, ast_annotation, problematic_node_id)
  problematic_node = template_tree.get_problematic_node()

  # 2 instantiate return_data
  return_data = {}
  return_data['problematic_node_type'] = problematic_node.get_type().split('.')[1]
  return_data['problematic_node_id'] = problematic_node.get_id()

  # 3 loop over a context
  context_node_cursor = problematic_node
  template_id = 0
  while context_node_cursor is not None:

    # 4 filter out invalid templates
    validation_result = validate_template(full_ast_text, context_node_cursor, template_id)
    if validation_result is not None:
      return_data[template_id] = validation_result
      template_id += 1
      context_node_cursor = context_node_cursor.get_parent()
      continue

    # 5 get the template for the current context
    template_dict = template_tree.v4_get_template_dict_for_node_id(problematic_node.get_id(), context_node_cursor.get_id(), lang)
    return_data[template_id] = {
      'template_id': template_id,
      'template_context': template_dict['template_context'],
      'template_context_str_repl': template_dict['template_context_str_repl'],
      'template_origin': template_dict['template_origin'],
      'templatized_node_ids': template_dict['templatized_node_ids'],
      'templatized_node_ids_context': template_dict['templatized_node_ids_context'],
      'context_node_type': context_node_cursor.get_type().split('.')[1],
      'is_valid_template': True,
      'is_insert_secret_fn': does_need_secret_fn_insertion(template_dict['template_context_str_repl']),
      'sub_templates': None,
      'contexts': parse_context_dict(contexts, template_id),
    }
    template_id += 1
    context_node_cursor = context_node_cursor.get_parent()

    # TODO break for now, save only the first template
    break

  return_data['num_templates'] = template_id
  with open('temporary_templates.json', 'w') as fout:
    fout.write(json.dumps(return_data))

  # NOTE uncomment if testing only templatization
  # raise RuntimeError

  return return_data


def validate_template(
  full_ast_text: list,
  context_node: PirelNode,
  template_id: int
) -> Union[dict, None]:
  '''
  Validate template.
  Return None if template is valid, dict otherwise.
  '''

  reference_tree_full = PirelTree(full_ast_text)
  reference_tree_full._fix_indentation()

  reference_template_node = reference_tree_full.get_node_with_id(context_node.get_id())
  reference_template_text = reference_template_node.get_text()

  if s_parse_utils.has_parse_error(reference_template_text, lang='py'):
    return {
      'template_id': template_id,
      'template_origin': reference_template_text,
      'context_node_type': context_node.get_type(),
      'template_origin_node_type': None,
      'is_valid_template': False,
      'error': 'parse error of template_origin'
    }

  reference_template_ast_text, _ = ast_parse.parse_text_dbg_keep_text(reference_template_text, 'py')
  reference_template_tree = PirelTree(reference_template_ast_text)

  error = None
  template_origin_node_type = reference_template_node.get_type()

  if s_parse_utils.has_parse_error(reference_template_text, parser=None, lang='py'):
    error = 'template origin has a parse error when parsed as it is'
  elif len(reference_template_tree.get_root_node().get_children()) > 1:
    error = 'template origin contains multiple nodes'
  elif not context_node.is_type_isomorphic_to(reference_template_tree.get_root_node().get_children()[0]):
    error = 'template origin is not type-isomorphic to the context node'
    template_origin_node_type = reference_template_tree.get_root_node().get_children()[0].get_type()

  # template is good
  if error is None:
    return None

  return {
    'template_id': template_id,
    'template_origin': reference_template_text,
    'context_node_type': context_node.get_type(),
    'template_origin_node_type': template_origin_node_type,
    'is_valid_template': False,
    'error': error
  }


def parse_context_dict(
  contexts: list,
  template_id: int
) -> list:
  '''
  '''
  template_contexts = []
  for context in contexts:
    source_context = context['source_context']
    target_context = context['target_context']

    source_context_prev_siblings = [] if template_id == 0 else source_context[0][1:]
    source_context_parents = list(map(lambda x: x[0], source_context[1:1+template_id]))
    target_context_prev_siblings = [] if template_id == 0 else target_context[0][1:]
    target_context_parents = list(map(lambda x: x[0], target_context[1:1+template_id]))

    template_contexts.append({
      'source_context': {'siblings': source_context_prev_siblings, 'parents': source_context_parents},
      'target_context': {'siblings': target_context_prev_siblings, 'parents': target_context_parents},
    })

  return template_contexts


def does_need_secret_fn_insertion(template: str) -> bool:
  '''
  NOTE current implementation is written with Python source code in mind.
  For other languages we may need different implementation.
  '''
  def _count_leading_spaces(text: str) -> int:
    return len(text) - len(text.lstrip(' '))
  def _get_indentations_set(lines: List[str]) -> List[int]:
    return list(set(map(_count_leading_spaces, lines)))
  lines = template.split('\n')
  assert len(lines) > 0
  if len(lines) == 1:
    return False
  if len(_get_indentations_set(lines)) > 1:
    return True
  return False
