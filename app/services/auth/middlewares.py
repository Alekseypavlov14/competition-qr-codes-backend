from services.auth.session import get_user_by_session_token
from shared.const import auth_header
from functools import wraps
from flask import request

def auth_required(function):
  @wraps(function)
  def decorated_function(*args, **kwargs):
    token = request.headers.get(auth_header)
    get_user_by_session_token(token)

    return function(*args, **kwargs)
  
  return decorated_function