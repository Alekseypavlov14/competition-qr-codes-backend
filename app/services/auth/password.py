import bcrypt

def validate_password(password: str, user_password: str):
  encoded_password = password.encode('utf-8')
  encoded_user_password = user_password.encode('utf-8')
  return bcrypt.checkpw(encoded_password, encoded_user_password)

def hash_password(password: str):
  encoded_password = password.encode('utf-8')
  hash = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
  return hash.decode('utf-8')