from shared.const import token_length
import random
import string

def generate_token() -> str:
  return generate_random_string_by_length(token_length)

def generate_random_string_by_length(length: int) -> str:
  characters = string.ascii_letters + string.digits
  token = ''.join(random.choice(characters) for _ in range(length))
  return token
