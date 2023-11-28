# DEBUG_VERBOSE = 1
# DEBUG_VERBOSE = -2
# DEBUG_VERBOSE = -10
# DEBUG_VERBOSE = -11
DEBUG_VERBOSE = -11

# PROFILING_TYPE = "cProfile"
# PROFILING_TYPE = None
PROFILING_TYPE = None

# PROFILING_OUTPUT_STYLE = "FILE"
# PROFILING_OUTPUT_STYLE = "TEXT"
PROFILING_OUTPUT_STYLE = "FILE"

# ENABLE_CYTHON_PROFILE = False
# ENABLE_CYTHON_PROFILE = True
ENABLE_CYTHON_PROFILE = False

HIT_UNEXPECTED_ERROR = False
HIT_UNEXPECTED_ERROR_MESSAGE = None

class NormalException(Exception):
  """Exception that is understood (not fatal/unexpected error) and handled elegantly"""
  pass

class UnderstoodException(Exception):
  """Exception that is understood (not fatal/unexpected error), but not handled elegantly"""
  pass

class TranslationRuleNotFoundException(Exception):
  '''
  Exception that is thrown in case DuoGlot does not find a suitable translation rule.

  One use case:
  If this exception is caught, signal a loop for automatic rule inference.
  '''
  def __init__(self, templates_dict: dict) -> None:
    super().__init__()
    self.templates_dict = templates_dict

  def get_templates_dict(self) -> dict:
    return self.templates_dict
