from tree_sitter import Language, Parser
from pathlib import Path
import logging
import json

import grammar


################################################################################################
#################################### INHERITED FROM DUOGLOT ####################################
################################################################################################
# to run DuoGlot backend in interpreted mode
# otherwise, compile using Cython
INTERPRET_MODE = True


################################################################################################
#################################### TREESITTER RELATED ########################################
################################################################################################
_language_paths = [
  './tree-sitter-util/tree-sitter-javascript',
  './tree-sitter-util/tree-sitter-python'
]
Language.build_library('build/my-languages.so', _language_paths)

_py_language = Language('build/my-languages.so', 'python')
_js_language = Language('build/my-languages.so', 'javascript')

_py_parser = Parser()
_js_parser = Parser()

_py_parser.set_language(_py_language)
_js_parser.set_language(_js_language)

PARSER_DICT = {
  'py': _py_parser,
  'js': _js_parser
}


################################################################################################
#################################### GRAMMAR RELATED ###########################################
################################################################################################
with open(_language_paths[1] + '/src/grammar.json') as fin:
  PY_GRAMMAR = json.loads(fin.read())
with open(_language_paths[0] + '/src/grammar.json') as fin:
  JS_GRAMMAR = json.loads(fin.read())

grammar.grm_preprocess('py', PY_GRAMMAR)
grammar.grm_preprocess('js', JS_GRAMMAR)

GRAMMAR_DICT = {
  'py': PY_GRAMMAR,
  'js': JS_GRAMMAR
}

PY_NOT_INLINED_NTS = grammar.grm_get_all_not_inlined_NTs(PY_GRAMMAR)
JS_NOT_INLINED_NTS = grammar.grm_get_all_not_inlined_NTs(JS_GRAMMAR)

NT_DICT = {
  'py': PY_NOT_INLINED_NTS,
  'js': JS_NOT_INLINED_NTS
}


################################################################################################
#################################### TEMPLATE EXTRACTION #######################################
################################################################################################
TEX_UPTO_DEPTH_BUILTIN_TOKEN = 3  # do not templatize a node if it contains a built-in token up to this depth
TEX_TEMPLATIZATION_DEPTH_THRESHOLD_TEMPLATE_NODE = 3  # templatize a template node if it exceeds this depth
TEX_TEMPLATIZATION_DEPTH_THRESHOLD_CONTEXT_NODE = 2  # templatize a context node if it exceeds this depth


################################################################################################
#################################### PIREL CONFIGS #############################################
################################################################################################
PLACEHOLDER_TEXT = '__'  # string representation of a hole
CONTEXT_PH_TEXT = '<|pirel_context_hole|>'
GENERIC_SECRET_FN = 'secret_fun_4071'
GENERIC_SECRET_FN_INVOCATION = GENERIC_SECRET_FN + '()'
PAR_PROG_PROB_NODE_REPLACE = 'pirel_replace_var'
PAR_PROG_DUMMY_IDENTIFIER = 'pirel_dummy_var'

PY_BUILT_IN_FUNCTIONS = {"abs", "aiter", "all", "anext", "any", "ascii", "bin", "bool", "breakpoint", "bytearray", "bytes", "callable", "chr", "classmethod", "compile", "complex", "delattr", "dict", "dir", "divmod", "enumerate", "eval", "exec", "filter", "float", "format", "frozenset", "getattr", "globals", "hasattr", "hash", "help", "hex", "id", "input", "int", "isinstance", "issubclass", "iter", "len", "list", "locals", "map", "max", "memoryview", "min", "next", "object", "oct", "open", "ord", "pow", "print", "property", "range", "repr", "reversed", "round", "set", "setattr", "slice", "sorted", "staticmethod", "str", "sum", "super", "tuple", "type", "vars", "zip"}
NON_TEMPLATIZABLE_GRAMMAR_TERMINALS = {"(", ")", "[", "]", "=", "{", "}"}

# template simplification
# max depth for a node before it's simplified
LLM_VAL_TS_MAX_DEPTH = 4

# best N TSPs from each configuration (will choose no more than this value)
TSP_BEST_N_PER_CONFIG = 3


################################################################################################
#################################### SP1 & SP2 UNIFICATION #####################################
################################################################################################
MATCH_TYPE_TEG = 'terminal_exact_grammar'  # grammar terminals such as ',', '.', '(', ')'
MATCH_TYPE_TES = 'terminal_exact_semantic'  # literals, identifiers
MATCH_TYPE_TSEC = 'terminal_exact_secret'  # secret function call
MATCH_TYPE_TV = 'terminal_val'
MATCH_TYPE_NTDS = 'nonterminal_dotstar'
MATCH_TYPE_NOMATCH = 'no_match'  # very bad -> no match


################################################################################################
############################# TSP CANDIDATE PENALTY CALCULATION ################################
################################################################################################
# first priority configuration that favors
# different node type matches at templatized nodes
PENALTY_COEFS_DEFAULT = {
  'max_match_depth': 1.0,         # increase to punish deep matches
  'mean_num_tokens': 1.0,         # increase to punish large number of tokens
  'should_replace': 1.0,          # TODO what this affects?
  'ast_width1': 1.0,              # increase to punish wide matches
  'grammar_terminals_only': 1.0,  # increase to punish nodes with grammar terminals only
  'tn_bias': 0.0,                 # increases penalty

  # 1 makes no difference
  # pos value increases the penalty by ~ (use to punish match type)
  # neg value decreases the penalty by ~ (use to reward match type)
  # abs(match_coef) ^ (sign(match_coef) * match_count)  ~
  'match_penalty_coefs': {
    MATCH_TYPE_TEG: 1,
    MATCH_TYPE_TES: 3,            # NOTE not used now
    MATCH_TYPE_TSEC: -10,
    MATCH_TYPE_TV: 20,
    MATCH_TYPE_NTDS: -20,
    MATCH_TYPE_NOMATCH: 1000,
  },

  'tns_penalties': 1.0,           # increases effect of tns_penalties on pair_penalty
  'match_penalty': 1.0,           # increases effect of match_penalty on pair_penalty
  'pair_bias': 0.0,               # increases pair_penalty
}

# second priority configuration that favors
# _val_ matches over
# different node type matches at templatized nodes
PENALTY_COEFS_2 = {
  'max_match_depth': 1.0,         # increase to punish deep matches
  'mean_num_tokens': 1.0,         # increase to punish large number of tokens
  'should_replace': 1.0,          # TODO what this affects?
  'ast_width1': 1.0,              # increase to punish wide matches
  'grammar_terminals_only': 1.0,  # increase to punish nodes with grammar terminals only
  'tn_bias': 0.0,                 # increases penalty

  # 1 makes no difference
  # pos value increases the penalty by ~ (use to punish match type)
  # neg value decreases the penalty by ~ (use to reward match type)
  # abs(match_coef) ^ (sign(match_coef) * match_count)  ~
  'match_penalty_coefs': {
    MATCH_TYPE_TEG: 1,
    MATCH_TYPE_TES: 3,            # NOTE not used now
    MATCH_TYPE_TSEC: -10,
    MATCH_TYPE_TV: -20,
    MATCH_TYPE_NTDS: 20,
    MATCH_TYPE_NOMATCH: 1000,
  },

  'tns_penalties': 1.0,           # increases effect of tns_penalties on pair_penalty
  'match_penalty': 1.0,           # increases effect of match_penalty on pair_penalty
  'pair_bias': 0.0,               # increases pair_penalty
}

PENALTY_COEFS_DICT = {
  'primary': PENALTY_COEFS_DEFAULT,
  'secondary': PENALTY_COEFS_2
}


################################################################################################
#################################### LLM CONFIGS ###############################################
################################################################################################
SIMPLIFICATION_MAX_RETRIES = 5

GENERATION_START_TEMPERATURE = 1.0
GENERATION_TEMPERATURE_INCREMENT = 0.02
GENERATION_TEMPERATURE_ROUND_DIGITS = 2
GENERATION_NUM_VARIANTS_IN_RESPONSE = 5
GENERATION_TWO_SRC_PROGRAMS_MAX_RETRIES = 5

LLM_DEFAULT_TEMPERATURE = 1.0
LLM_DEFAULT_MODEL_NAME = 'gpt-4'
LLM_DEFAULT_MAX_TOKENS = 4096
LLM_DEFAULT_REQUEST_TIMEOUT = None
LLM_DEFAULT_MAX_RETRIES = 2
LLM_DEFAULT_NUM_COMPLETIONS = 5

TRANSLATION_SP1_MAX_RETRIES = 5
TRANSLATION_SP2_MAX_RETRIES = 3


################################################################################################
#################################### GENERAL CONFIGS ###########################################
################################################################################################
LANG_DICT = {
  'py': 'Python',
  'js': 'JavaScript'
}


################################################################################################
#################################### DIRECTORIES ###############################################
################################################################################################
CWD = Path(__file__).parent
LOGS_DIR = CWD / 'pirel-logs'


################################################################################################
#################################### LOGGING ###################################################
################################################################################################
LOG_FPATH = LOGS_DIR / 'pirel.log'
LOG_FMODE = 'a'
LOG_FORMAT = '%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s'
LOG_DATE_FORMAT = '%H:%M:%S'
LOG_LEVEL = logging.DEBUG
LOG_3RDPARTY_MODULES = ['werkzeug', 'httpx', 'openai._base_client', 'httpcore.connection', 'httpcore.http11']
LOG_3RDPARTY_LEVEL = logging.ERROR
