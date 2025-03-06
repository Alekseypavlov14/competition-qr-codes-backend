from functools import wraps
from flask import request
from services.auth.session import get_user_by_session_token

def auth_required(function):
  @wraps(function)
  def decorated_function(*args, **kwargs):
    token = request.headers.get('Authorization')
    get_user_by_session_token(token)

    return function(*args, **kwargs)
  
  return decorated_function