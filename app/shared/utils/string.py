import secrets

def generate_random_string_by_length(length: int) -> str:
  return secrets.token_hex(length // 2)
