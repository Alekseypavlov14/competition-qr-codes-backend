from services.auth.token import generate_token
from models.session import Session

def create_session(user_id: int):
  token = generate_token()
  session = Session(user_id=user_id, token=token)
  return session
