from services.auth.token import generate_token
from api.exceptions import UnauthorizedException
from models.session import Session
from models.user import User

def create_session(user_id: int):
  token = generate_token()
  session = Session(user_id=user_id, token=token)
  return session

def get_user_session_by_token(token: str):
  session = Session.query.filter_by(token=token).first()
  if not session: raise UnauthorizedException

  return session
