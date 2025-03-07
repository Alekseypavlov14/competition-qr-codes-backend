from services.auth.session import get_user_by_session_token
from services.auth.headers import get_auth_header
from api.exceptions import UnauthorizedException
from functools import wraps

def auth_required(function):
  @wraps(function)
  def decorated_function(*args, **kwargs):
    token = get_auth_header()
    if not token: raise UnauthorizedException
    
    get_user_by_session_token(token)

    return function(*args, **kwargs)
  
  return decorated_function