from services.auth.credentials import Credentials
from services.auth.password import validate_password, hash_password
from services.auth.session import create_session
from api.exceptions import ConflictException, UnauthorizedException
from models.user import User
from models.session import Session
from db import db

def sign_in(credentials: Credentials) -> str:
  user = User.query.filter_by(email=credentials.email).first()
  if not user: raise UnauthorizedException
  
  validation = validate_password(credentials.password, user.password)
  if not validation: raise UnauthorizedException

  old_session = Session.query.filter_by(user_id=user.id).first()
  if old_session: db.session.delete(old_session)

  new_session = create_session(user.id)
  db.session.add(new_session)

  db.session.commit()

  return new_session.token

def sign_up(credentials: Credentials) -> str:
  user_with_same_email = User.query.filter_by(email=credentials.email).first()
  if user_with_same_email: raise ConflictException

  hashed_password = hash_password(credentials.password)

  user = User(email=credentials.email,password=hashed_password)
  db.session.add(user)

  saved_user = User.query.filter_by(email=credentials.email).first()
  if not saved_user: raise ConflictException

  new_session = create_session(saved_user.id)
  db.session.add(new_session)

  db.session.commit()

  return new_session.token
