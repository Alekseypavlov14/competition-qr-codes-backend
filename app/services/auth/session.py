from services.auth.token import generate_token
from api.exceptions import NotFoundException
from models.session import Session
from models.user import User

def create_session(user_id: int):
  token = generate_token()
  session = Session(user_id=user_id, token=token)
  return session

def get_user_by_session_token(token: str):
  user = User.query.filter_by(session=token).first()
  if not user: raise NotFoundException

  return user
