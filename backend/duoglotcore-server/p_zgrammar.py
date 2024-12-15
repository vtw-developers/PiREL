import json


class TreeSitterGrammar:
  '''
  Parse Tree-sitter grammar.json file
  Example file: https://github.com/tree-sitter/tree-sitter-python/blob/master/src/grammar.json

  Can be fully automated by first parsing the grammar-schema.json file
  https://github.com/tree-sitter/tree-sitter/blob/master/cli/src/generate/grammar-schema.json
  However, to keep it simple at the beginning, grammar-schema.json will be hard-coded.

  PRINCIPLE
  The grammar is stored as it appears in grammar.json

  INTERNAL
  rule = rule_name: rule
  '''

  def __init__(self, grammar_dict: dict) -> None:
    '''
    PARAMS
    grammar_dict - grammar.json file parsed as dict

    INTERNAL
    self.name - grammar name
    self.rules - dict of rules
    '''

    # required by grammar-schema.json
    assert 'name' in grammar_dict
    assert 'rules' in grammar_dict
    self.name = grammar_dict['name']
    self.rules = grammar_dict['rules']

    # extras
    self.extras = None
    if 'extras' in grammar_dict:
      self.extras = grammar_dict['extras']

    # externals
    self.externals = None
    if 'externals' in grammar_dict:
      self.externals = grammar_dict['externals']

    # inline
    self.inline = None
    if 'inline' in grammar_dict:
      self.inline = grammar_dict['inline']

    # conflicts
    self.conflicts = None
    if 'conflicts' in grammar_dict:
      self.conflicts = grammar_dict['conflicts']

    # supertypes
    self.supertypes = None
    if 'supertypes' in grammar_dict:
      self.supertypes = grammar_dict['supertypes']

    # precedences
    self.precedences = None
    if 'precedences' in grammar_dict:
      self.precedences = grammar_dict['precedences']

  def get_rule(self, rule_name: str) -> dict:
    assert rule_name in self.rules, 'the rule does not exist'
    return self.rules[rule_name]

  # boolean methods for simple rules
  def is_blank_rule(self, rule: dict) -> bool:
    return rule['type'] == 'BLANK'

  def is_string_rule(self, rule: dict) -> bool:
    return rule['type'] == 'STRING'

  def is_pattern_rule(self, rule: dict) -> bool:
    return rule['type'] == 'PATTERN'

  def is_symbol_rule(self, rule: dict) -> bool:
    return rule['type'] == 'SYMBOL'

  def is_seq_rule(self, rule: dict) -> bool:
    return rule['type'] == 'SEQ'

  def is_choice_rule(self, rule: dict) -> bool:
    return rule['type'] == 'CHOICE'

  def is_alias_rule(self, rule: dict) -> bool:
    return rule['type'] == 'ALIAS'

  def is_repeat_rule(self, rule: dict) -> bool:
    return rule['type'] == 'REPEAT'

  def is_repeat1_rule(self, rule: dict) -> bool:
    return rule['type'] == 'REPEAT1'

  def is_token_rule(self, rule: dict) -> bool:
    return rule['type'] in ['TOKEN', 'IMMEDIATE_TOKEN']

  def is_field_rule(self, rule: dict) -> bool:
    return rule['type'] == 'FIELD'

  def is_prec_rule(self, rule: dict) -> bool:
    return rule['type'] in ['PREC', 'PREC_LEFT', 'PREC_RIGHT', 'PREC_DYNAMIC']

  # boolean methods for compound rules
  def is_optional_rule(self, rule: dict) -> bool:

    # rule must be choice
    if not self.is_choice_rule(rule):
      return False

    members = rule['members']

    # choice b/w two elements
    if len(members) != 2:
      return False

    blank_rules = filter(lambda rule: self.is_blank_rule(rule), members)

    if len(blank_rules) != 1:
      return False

    return True

  def is_commaSep1_rule(self, rule: dict) -> bool:
    ''''''

  def is_sep1_rule(self, rule: dict) -> bool:
    ''''''


# NOTE this is a temporary function, can be removed later
def make_rule_paths():
  with open('temporary_python-grammar.json') as fin:
    grammar_dict = json.loads(fin.read())
  grammar_py = TreeSitterGrammar(grammar_dict)

  '''
  {
    (module, _statement): {
      1: repeat
    },
    (_statement, _simple_statements): {
      1: choice
    },
    (_statement, _compound_statements): {
      1: choice
    }
  }

  {
    module: {
      _statement: {
        1: [(repeat _statement)]
      },
      _simple_statements: {
        2: [(repeat _statement), (choice _simple_statements)]
      },
      _compound_statements: {
        2: [(repeat _statement), (choice _compound_statements)]
      }
    },
    _statement: {
      _simple_statements: {
        1: [(choice _simple_statements)]
      },
      _compound_statements: {
        1: [(choice _compound_statements)]
      }
    },
    _simple_statements: {
      _simple_statement: {
        1: [(sep1 _simple_statement ";")]
      }
      // stopped here
    }
  }
  '''

  for rule in grammar_py.rules:
    pass


def test_grammar():
  with open('temporary_python-grammar.json') as fin:
    grammar_dict = json.loads(fin.read())
  grammar_py = TreeSitterGrammar(grammar_dict)


if __name__ == '__main__':
  test_grammar()
