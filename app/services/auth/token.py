from shared.utils.string import generate_random_string_by_length
from shared.const import token_length

def generate_token() -> str:
  return generate_random_string_by_length(token_length)
